from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TELEGRAM_TOKEN =8346701498:AAHRz3zckfQlkHVTFUdQrimvOzjxe5PCf_U

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔥 IA EXTREMA ONLINE!")

async def sinais(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = """
🚨 IA EXTREMA 🚨

⚽ Benfica vs Porto
🎯 Empate
📈 Confiança: 78%

⚽ Arsenal vs Chelsea
🎯 Vitória Arsenal
📈 Confiança: 83%
"""
    await update.message.reply_text(texto)

app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("sinais", sinais))

print("Bot online...")
app.run_polling()
