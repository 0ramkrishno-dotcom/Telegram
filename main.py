from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_photo(chat_id=update.effective_chat.id,photo=("https://i.postimg.cc/W3WTyJYM/IMG-1785647969787.jpg")

if __name__ == '__main__':
    # আপনার এপিআই টোকেনটি এখানে বসান
    application = ApplicationBuilder().token('8601353590:AAE6NCllJV1Rhy_pQns9PpJgdyaShwxtTec').build()
    
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    
    application.run_polling()
