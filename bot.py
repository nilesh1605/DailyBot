import logging
import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

BOT_TOKEN = os.getenv("BOT_TOKEN")
print("BOT_TOKEN VALUE:", BOT_TOKEN)
print("BOT_TOKEN LENGTH:", len(BOT_TOKEN) if BOT_TOKEN else "NONE")
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

main_menu = ReplyKeyboardMarkup(
    [
        ["Today Earning Idea"],
        ["Online Work Websites"],
        ["Money Saving Tips"],
        ["Free AI Tools to Earn"],
        ["Motivation Boost"],
    ],
    resize_keyboard=True
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "Welcome to Daily Money Ideas Bot!\n\n"
        "Learn ways to earn online and grow your income.\n\n"
        "Choose an option below."
    )
    await update.message.reply_text(text, reply_markup=main_menu)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text

    if user_text == "Today Earning Idea":
        await update.message.reply_text("Sell Canva templates and list them on Fiverr or Etsy.")

    elif user_text == "Online Work Websites":
        await update.message.reply_text("Fiverr, Upwork, Freelancer, Etsy, Amazon KDP.")

    elif user_text == "Money Saving Tips":
        await update.message.reply_text("Track every expense for 7 days to find waste.")

    elif user_text == "Free AI Tools to Earn":
        await update.message.reply_text("ChatGPT, Canva AI, CapCut, Remove.bg, Leonardo AI.")

    elif user_text == "Motivation Boost":
        await update.message.reply_text("Your phone can become your income machine.")

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()
