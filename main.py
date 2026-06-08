from bot import Bot
import pyrogram.utils
from flask import Flask
from threading import Thread
import os

pyrogram.utils.MIN_CHANNEL_ID = -1009147483647

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'UNRATED CODER FileStore'

def run():
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)

if __name__ == "__main__":
    Thread(target=run, daemon=True).start()
    try:
        Bot().run()
    except Exception as e:
        print(f"Error starting bot: {e}")
        # Keep the main thread alive so the Flask thread continues to run
        import time
        while True:
            time.sleep(3600)
