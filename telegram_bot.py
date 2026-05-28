from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8346701498:AAFgFEzEHRx1NBZo5IUWPocW3dI31JzUqMo"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot online!")

async def sinais(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "⚽ Benfica vs Porto\n🎯 Empate\n📈 78%"
    )

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("sinais", sinais))

print("Bot online")
app.run_polling()
