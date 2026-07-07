python
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Agent Online. Awaiting directive.")

if __name__ == "__main__":
    # Replace 'YOUR_TOKEN' with the one from BotFather
    app = ApplicationBuilder().token("YOUR_TOKEN").build()
    app.add_handler(CommandHandler("start", start))
    print("Agent heartbeat active...")
    app.run_polling()
