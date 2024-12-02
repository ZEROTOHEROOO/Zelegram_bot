import telegram
from telegram.ext import Updater, CommandHandler

# Replace with your bot token
BOT_TOKEN = "YOUR_BOT_TOKEN"

def start(update, context):
    update.message.reply_text("*Welcome! to ZERO!BOT!* 
    *I promise to guide you from Zero to Hero in programming! 🚀* 

 *Whether you're a complete beginner or looking to master advanced topics, I’ll provide step-by-step tutorials, coding exercises, and resources to help you grow your skills.* 
 *Learning programming can feel overwhelming, but don’t worry—I'm here to help!* 
 *Let's start your journey towards becoming a programming pro! Type /start to begin.*)

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
