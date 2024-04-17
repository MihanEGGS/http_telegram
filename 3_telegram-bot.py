# 
# https://docs.python-telegram-bot.org/en/v21.0.1/index.html
# 
# 1. Uzinstalē bibliotēku
# > pip3 install python-telegram-bot
# 
# 2. Uztaisi jaunu Telegram botu un saņem "token" - https://core.telegram.org/bots/features#creating-a-new-bot
#
# 3. Samaini kodā YOUR_TOKEN ar savu token
# 
# 4. Palaid kodu un ieraksti čatā /start
# 
# 5. Apskaties citas komandas - /hello un /echo
#
# 6. Izmantojot kodu no iepriekšēja piemēra (1_faker.py), izveido jaunu komandu /fakeperson, kura uzģenerē personas vārdu, uzvārdu ar telefona numuru, adresi un personas kodu
# 
# 7. Izmantojot kodu no iepriekšēja piemēra (2_chuck_norris.py), izveido jaunu komandu /chuck, kura uzģenerē jaunu joku par programmetājiem
from faker import Faker
fake = Faker()
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import requests
# izveido bota pieslēgumu Telegram
app = ApplicationBuilder().token("7112507583:AAGIDFfC-NsKjdeX_T1uj0_nOdvlps1oBas").build()

# komanda /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("I'm test bot. Type /hello or /echo")

# komanda /hello
async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(update.effective_user)
    await update.message.reply_text("Hello", update.effective_user.first_name, " ", update.effective_user.last_name)

# komanda /echo
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("I hear: " + update.message.text)
async def fakeperson(update: Update, context: ContextTypes.DEFAULT_TYPE):
     await update.message.reply_text(fake.name()  +fake.country_calling_code() + fake.phone_number()+ fake.address()+ fake.ssn())
async def chuck(update: Update, context: ContextTypes.DEFAULT_TYPE):
    r = requests.get('https://api.chucknorris.io/jokes/random')
    jokes = r.json()
    await update.message.reply_text(jokes['value'])

# savieno čata komandu ar funkciju
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("echo", echo))
app.add_handler(CommandHandler("fakeperson", fakeperson))
app.add_handler(CommandHandler("chuck", chuck))

# sāk bota darbību
app.run_polling()
