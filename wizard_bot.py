import logging
import random
from telegram import Update
from telegram.ext import (Application, CommandHandler, ContextTypes, MessageHandler, filters)
import os
from dotenv import load_dotenv

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger('wizard_bot')

predictionsRu = [
  'Безусловно',
  'Абсолютно точно',
  'Никаких сомнений',
  'Определенно да',
  'Можешь положиться на это',
  'Мне кажется да',
  'Скорее всего',
  'Перспективы неплохи',
  'Знаки говорят да',
  'Да',
  'Пока не ясно, попробуй снова',
  'Спроси позже',
  'Не хочу об этом сейчас',
  'Сейчас не могу сказать',
  'Подумай и спроси снова',
  'Даже не думай',
  'Мой ответ: нет',
  'По моим данным нет',
  'Перспективы не очень хороши',
  'Очень сомневаюсь'
]
introduction = "Вы в присутствии настоящего предсказателя! \
Я могу ответить на любой вопрос на который можно ответить да или нет,\
 но только если вы обращаетесь ко мне 'Волшебник'."

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(introduction)   

async def msg(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    a = len(predictionsRu)
    b = random.randint(0, a - 1)
    await update.message.reply_text(predictionsRu[b])
    

def main() -> None:
    load_dotenv()
    api_key = os.getenv("API_KEY")
    """Run the bot."""
    application = Application.builder().token(api_key).build()
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(MessageHandler(filters.Regex(r"^Волшебник"), msg))
    application.run_polling()
    


main()