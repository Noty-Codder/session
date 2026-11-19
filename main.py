import config
import time
import random
import logging
from pyrogram import Client, idle
from pyromod import listen  
from pyrogram.errors import ApiIdInvalid, ApiIdPublishedFlood, AccessTokenInvalid

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

logging.getLogger("pymongo").setLevel(logging.ERROR)
logger = logging.getLogger("StringGenBot")

# ANSI colors for the console banner (a fresh one is picked every run)
ANSI_COLORS = ["\033[91m", "\033[92m", "\033[93m", "\033[94m", "\033[95m", "\033[96m"]
RESET = "\033[0m"


def colorize(text: str) -> str:
    color = random.choice(ANSI_COLORS)
    return f"{color}{text}{RESET}"


# Initialize start time
StartTime = time.time()

# Initialize the Client
app = Client(
    "Anonymous",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN,
    in_memory=True,
    plugins=dict(root="StringGenBot"),
)

if __name__ == "__main__":
    print(colorize("Session Gen Bot is starting..."))
    logger.info("Startup sequence initiated.")
    try:
        app.start()
    except ApiIdInvalid:
        raise Exception("Your API_ID is not valid.")
    except ApiIdPublishedFlood:
        raise Exception("Your API_ID/API_HASH is flood banned.")
    except AccessTokenInvalid:
        raise Exception("Your BOT_TOKEN is not valid.")
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
        raise

    uname = app.get_me().username
    print(colorize(f"@{uname} is online and ready to generate string sessions."))
    logger.info(f"Bot started successfully as @{uname}.")

    idle()

    app.stop()
    print(colorize("Session Gen Bot has stopped."))
    logger.info("Bot stopped.")
