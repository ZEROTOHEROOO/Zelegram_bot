import telegram
from telegram.ext import Updater, CommandHandler

# Replace with your bot token
BOT_TOKEN = "YOUR_BOT_TOKEN"

def start(update, context):
    update.message.reply_text("*Welcome! to ZERO!BOT!")
def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    # Add command handler
    dp.add_handler(CommandHandler("start", start))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
