
# Mego AI Prompt Bot (GitHub Deployment Ready)

A Telegram bot that generates creative ChatGPT prompts from user messages. It supports multiple languages and lets users export their prompt history.

## Features
- ✨ Creative prompt style
- 🌍 Multilingual input detection
- 💾 Export prompt history (/export command)

## How to Use

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/mego-ai-prompt-bot.git
cd mego-ai-prompt-bot
```

### 2. Set up environment

Rename `.env.example` to `.env` and fill in your credentials:

```env
BOT_TOKEN=your_telegram_token
OPENAI_API_KEY=your_openai_key
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the bot

```bash
python main.py
```

## Deploying on Railway or Replit

This repo is ready for Railway and Replit out-of-the-box. Just add `BOT_TOKEN` and `OPENAI_API_KEY` as environment variables.

---
