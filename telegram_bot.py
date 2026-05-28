
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from app.services.ia_engine import gerar_sinais
from app.config import TELEGRAM_TOKEN

async def sinais(update: Update, context: ContextTypes.DEFAULT_TYPE):
    dados = gerar_sinais()

    texto = "🚨 IA EXTREMA - SINAIS\n\n"

    for item in dados:
        texto += (
            f"⚽ {item['jogo']}\n"
            f"🎯 {item['previsao']}\n"
            f"📈 Confiança: {item['confianca']}\n\n"
        )

    await update.message.reply_text(texto)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔥 IA EXTREMA ativa. Usa /sinais"
    )

app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("sinais", sinais))

print("Bot online...")
app.run_polling()
