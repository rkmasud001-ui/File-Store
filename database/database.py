#Codeflix_Botz
#rohit_1888 on Tg

import motor, asyncio
import motor.motor_asyncio
import time
import pymongo, os
from config import DB_URI, DB_NAME
from bot import Bot
import logging
from datetime import datetime, timedelta
from functools import wraps

try:
    dbclient = pymongo.MongoClient(DB_URI)
    database = dbclient[DB_NAME]
except Exception as e:
    logging.error(f"Error connecting to Pymongo: {e}")
    dbclient = None
    database = None

logging.basicConfig(level=logging.INFO)

def connection_check(default_return=None):
    def decorator(func):
        @wraps(func)
        async def wrapper(self, *args, **kwargs):
            if not self.database:
                return default_return
            return await func(self, *args, **kwargs)
        return wrapper
    return decorator

class Rohit:

    def __init__(self, DB_URI, DB_NAME):
        try:
            self.dbclient = motor.motor_asyncio.AsyncIOMotorClient(DB_URI)
            self.database = self.dbclient[DB_NAME]
        except Exception as e:
            logging.error(f"Error connecting to Motor: {e}")
            self.dbclient = None
            self.database = None

        if self.database is not None:
            self.channel_data = self.database['channels']
            self.admins_data = self.database['admins']
            self.user_data = self.database['users']
            self.banned_user_data = self.database['banned_user']
            self.autho_user_data = self.database['autho_user']
            self.del_timer_data = self.database['del_timer']
            self.fsub_data = self.database['fsub']
            self.rqst_fsub_data = self.database['request_forcesub']
            self.rqst_fsub_Channel_data = self.database['request_forcesub_channel']
        else:
            self.channel_data = None
            self.admins_data = None
            self.user_data = None
            self.banned_user_data = None
            self.autho_user_data = None
            self.del_timer_data = None
            self.fsub_data = None
            self.rqst_fsub_data = None
            self.rqst_fsub_Channel_data = None


    # USER DATA
    @connection_check(default_return=False)
    async def present_user(self, user_id: int):
        found = await self.user_data.find_one({'_id': user_id})
        return bool(found)

    @connection_check()
    async def add_user(self, user_id: int):
        await self.user_data.insert_one({'_id': user_id})
        return

    @connection_check(default_return=[])
    async def full_userbase(self):
        user_docs = await self.user_data.find().to_list(length=None)
        user_ids = [doc['_id'] for doc in user_docs]
        return user_ids

    @connection_check()
    async def del_user(self, user_id: int):
        await self.user_data.delete_one({'_id': user_id})
        return


    # ADMIN DATA
    @connection_check(default_return=False)
    async def admin_exist(self, admin_id: int):
        found = await self.admins_data.find_one({'_id': admin_id})
        return bool(found)

    @connection_check()
    async def add_admin(self, admin_id: int):
        if not await self.admin_exist(admin_id):
            await self.admins_data.insert_one({'_id': admin_id})
            return

    @connection_check()
    async def del_admin(self, admin_id: int):
        if await self.admin_exist(admin_id):
            await self.admins_data.delete_one({'_id': admin_id})
            return

    @connection_check(default_return=[])
    async def get_all_admins(self):
        users_docs = await self.admins_data.find().to_list(length=None)
        user_ids = [doc['_id'] for doc in users_docs]
        return user_ids


    # BAN USER DATA
    @connection_check(default_return=False)
    async def ban_user_exist(self, user_id: int):
        found = await self.banned_user_data.find_one({'_id': user_id})
        return bool(found)

    @connection_check()
    async def add_ban_user(self, user_id: int):
        if not await self.ban_user_exist(user_id):
            await self.banned_user_data.insert_one({'_id': user_id})
            return

    @connection_check()
    async def del_ban_user(self, user_id: int):
        if await self.ban_user_exist(user_id):
            await self.banned_user_data.delete_one({'_id': user_id})
            return

    @connection_check(default_return=[])
    async def get_ban_users(self):
        users_docs = await self.banned_user_data.find().to_list(length=None)
        user_ids = [doc['_id'] for doc in users_docs]
        return user_ids



    # AUTO DELETE TIMER SETTINGS
    @connection_check()
    async def set_del_timer(self, value: int):        
        existing = await self.del_timer_data.find_one({})
        if existing:
            await self.del_timer_data.update_one({}, {'$set': {'value': value}})
        else:
            await self.del_timer_data.insert_one({'value': value})

    @connection_check(default_return=0)
    async def get_del_timer(self):
        data = await self.del_timer_data.find_one({})
        if data:
            return data.get('value', 600)
        return 0


    # CHANNEL MANAGEMENT
    @connection_check(default_return=False)
    async def channel_exist(self, channel_id: int):
        found = await self.fsub_data.find_one({'_id': channel_id})
        return bool(found)

    @connection_check()
    async def add_channel(self, channel_id: int):
        if not await self.channel_exist(channel_id):
            await self.fsub_data.insert_one({'_id': channel_id})
            return

    @connection_check()
    async def rem_channel(self, channel_id: int):
        if await self.channel_exist(channel_id):
            await self.fsub_data.delete_one({'_id': channel_id})
            return

    @connection_check(default_return=[])
    async def show_channels(self):
        channel_docs = await self.fsub_data.find().to_list(length=None)
        channel_ids = [doc['_id'] for doc in channel_docs]
        return channel_ids

    
# Get current mode of a channel
    @connection_check(default_return="off")
    async def get_channel_mode(self, channel_id: int):
        data = await self.fsub_data.find_one({'_id': channel_id})
        return data.get("mode", "off") if data else "off"

    # Set mode of a channel
    @connection_check()
    async def set_channel_mode(self, channel_id: int, mode: str):
        await self.fsub_data.update_one(
            {'_id': channel_id},
            {'$set': {'mode': mode}},
            upsert=True
        )

    # REQUEST FORCE-SUB MANAGEMENT

    # Add the user to the set of users for a   specific channel
    @connection_check()
    async def req_user(self, channel_id: int, user_id: int):
        try:
            await self.rqst_fsub_Channel_data.update_one(
                {'_id': int(channel_id)},
                {'$addToSet': {'user_ids': int(user_id)}},
                upsert=True
            )
        except Exception as e:
            print(f"[DB ERROR] Failed to add user to request list: {e}")


    # Method 2: Remove a user from the channel set
    @connection_check()
    async def del_req_user(self, channel_id: int, user_id: int):
        # Remove the user from the set of users for the channel
        await self.rqst_fsub_Channel_data.update_one(
            {'_id': channel_id}, 
            {'$pull': {'user_ids': user_id}}
        )

    # Check if the user exists in the set of the channel's users
    @connection_check(default_return=False)
    async def req_user_exist(self, channel_id: int, user_id: int):
        try:
            found = await self.rqst_fsub_Channel_data.find_one({
                '_id': int(channel_id),
                'user_ids': int(user_id)
            })
            return bool(found)
        except Exception as e:
            print(f"[DB ERROR] Failed to check request list: {e}")
            return False  


    # Method to check if a channel exists using show_channels
    async def reqChannel_exist(self, channel_id: int):
    # Get the list of all channel IDs from the database
        channel_ids = await self.show_channels()
        #print(f"All channel IDs in the database: {channel_ids}")

    # Check if the given channel_id is in the list of channel IDs
        if channel_id in channel_ids:
            #print(f"Channel {channel_id} found in the database.")
            return True
        else:
            #print(f"Channel {channel_id} NOT found in the database.")
            return False


db = Rohit(DB_URI, DB_NAME)
