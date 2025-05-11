
from telegram import Update, InputFile
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from langdetect import detect
import openai
import json
import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
openai.api_key = os.getenv("OPENAI_API_KEY")

user_prompts = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Send me your idea or message in any language, and I'll turn it into a creative ChatGPT prompt!")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = str(update.message.from_user.id)
    user_input = update.message.text
    lang = detect(user_input)

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a creative assistant who rewrites user input into imaginative, engaging prompts for ChatGPT. Reply in the same language as the input."},
            {"role": "user", "content": user_input}
        ]
    )
    creative_prompt = response['choices'][0]['message']['content']

    if user_id not in user_prompts:
        user_prompts[user_id] = []
    user_prompts[user_id].append({"original": user_input, "prompt": creative_prompt})

    await update.message.reply_text(creative_prompt)

async def export_prompts(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = str(update.message.from_user.id)
    if user_id not in user_prompts or not user_prompts[user_id]:
        await update.message.reply_text("❌ You don't have any saved prompts.")
        return

    file_path = f"{user_id}_prompts.json"
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(user_prompts[user_id], f, ensure_ascii=False, indent=2)

    await update.message.reply_document(InputFile(file_path))
    os.remove(file_path)

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("export", export_prompts))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

app.run_polling()
