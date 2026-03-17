# Telegram File Store Bot

A simple yet powerful Telegram File Store Bot to save and share files via special links.

## Credits
Modified and maintained by [@UNRATED_CODER FROM TG!](https://t.me/UNRATED_CODER)

## Features
- Save files from a database channel.
- Generate permanent links for files.
- Force subscription support.
- Flask web server for health checks.
- Compatible with all hosting platforms (Render, Heroku, Koyeb, VPS, etc.).

## Available Commands

### User Commands
- `/start` - Start the bot.
- `/help` - Get help information.
- `/about` - About the bot.

### Admin Commands
- `/commands` - List all available admin commands.
- `/stats` - Get bot statistics.
- `/users` - Get the number of users in the database.
- `/dlt_time` - Set auto-delete time for files.
- `/check_dlt_time` - Check the current auto-delete time.
- `/broadcast` - Broadcast a message to all users.
- `/pbroadcast` - Broadcast a photo to all users.
- `/dbroadcast` - Broadcast a document/video to all users.
- `/batch` - Create a batch of file links.
- `/genlink` - Generate a single file link.
- `/custom_batch` - Create a custom batch of file links.
- `/ban` - Ban a user.
- `/unban` - Unban a user.
- `/banlist` - List all banned users.
- `/addchnl` - Add a force-subscription channel.
- `/delchnl` - Remove a force-subscription channel.
- `/listchnl` - List all force-subscription channels.
- `/fsub_mode` - Toggle force-subscription mode.
- `/add_admin` - Add a new admin.
- `/deladmin` - Remove an admin.
- `/admins` - List all admins.

## Hosting Compatibility
This bot is designed to work seamlessly across multiple platforms:

- **Render / Koyeb / VPS**: Uses a Flask server on a configurable `PORT` to pass health checks.
- **Heroku**: Uses a `Procfile` with a `web` process to bind to the dynamic `$PORT` provided by Heroku.

## Deployment
1. Set up your environment variables in your hosting provider's dashboard.
2. The bot will automatically bind to the `PORT` provided by the environment.
3. Run command: `python3 main.py`.

## Support
Join our Telegram channel for updates and support: [@UNRATED_CODER](https://t.me/UNRATED_CODER)
