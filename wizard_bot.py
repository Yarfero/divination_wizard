import logging
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove, Update, InlineKeyboardButton, InlineKeyboardMarkup)
from telegram.ext import (Application, CallbackQueryHandler, CommandHandler, ContextTypes, ConversationHandler, MessageHandler, filters)
import os
from dotenv import load_dotenv

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger('wizard_bot')

async def msg(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("А?")

def main() -> None:
    load_dotenv()
    api_key = os.getenv("API_KEY")
    """Run the bot."""
    application = Application.builder().token(api_key).build()
    application.add_handler(MessageHandler(filters.Regex(r"^Волшебник"), msg))
    application.run_polling()
    

if __name__ == 'main':
    main()