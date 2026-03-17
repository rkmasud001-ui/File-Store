from bot import Bot
import pyrogram.utils
from flask import Flask
from threading import Thread
from config import PORT

pyrogram.utils.MIN_CHANNEL_ID = -1009147483647

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'UNRATED CODER FileStore'

def run():
    app.run(host="0.0.0.0", port=int(PORT))

if __name__ == "__main__":
    Thread(target=run).start()
    Bot().run()
