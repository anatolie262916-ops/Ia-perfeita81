from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import requests

TOKEN = "8346701498:AAFgFEzEHRx1NBZo5PocW3dI31JzUqMo"

API_KEY = "2b531680236346b5bbb44c2d2c1255f6"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot de sinais online ⚽")

async def sinais(update: Update, context: ContextTypes.DEFAULT_TYPE):

    url = "https://v3.football.api-sports.io/fixtures?live=all"

    headers = {
        'x-apisports-key': API_KEY
    }

    response = requests.get(url, headers=headers)

    data = response.json()

    jogos = data.get("response", [])

    if not jogos:
        await update.message.reply_text("Sem jogos ao vivo.")
        return

    mensagem = ""

    for jogo in jogos[:5]:

        casa = jogo["teams"]["home"]["name"]
        fora = jogo["teams"]["away"]["name"]

        golos_casa = jogo["goals"]["home"]
        golos_fora = jogo["goals"]["away"]

        mensagem += f"{casa} {golos_casa} - {golos_fora} {fora}\n"

    await update.message.reply_text(mensagem)

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("sinais", sinais))

app.run_polling()
