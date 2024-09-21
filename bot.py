import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the API token from .env file
token = os.getenv("TELEGRAM_API_TOKEN")

from telegram import Update
from telegram.ext import Application, CommandHandler

# Function to handle /start command
async def start(update: Update, context):
    await update.message.reply_text('Hello! I am your bot.')

# Create the bot application
async def main():
    application = Application.builder().token(token).build()

    # Add command handler for the /start command
    application.add_handler(CommandHandler("start", start))

    # Start the bot
    await application.start_polling()
    await application.idle()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())

