# Telegram X.com to StupidPenisX.com Link Replacer Bot

A Telegram bot that automatically replaces x.com links with stupidpenisx.com links to provide better Twitter embeds in groups and channels.

## Features

- 🔄 Automatically detects x.com and twitter.com links in messages
- 📝 Replies with stupidpenisx.com versions for better embeds
- 🛡️ Works in groups, supergroups, and channels
- ⚡ Fast and lightweight
- 📊 Built-in logging and error handling
- 🔐 Secure token management

## Quick Start

### 1. Create a Telegram Bot

1. Message [@BotFather](https://t.me/botfather) on Telegram
2. Use `/newbot` command and follow the instructions
3. Save your bot token

### 2. Setup Environment

```bash
# Clone or download this project
cd x-embeder-tg-bot

# Create virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create environment file
cp .env.example .env
```

### 3. Configure Bot Token

Edit `.env` file and add your bot token:

```env
TELEGRAM_BOT_TOKEN=your_bot_token_here
```

### 4. Run the Bot

```bash
python bot.py
```

## Usage

1. **Add the bot to your group/channel**
   - Search for your bot username
   - Add it to the desired group or channel
   - Grant it "Read Messages" and "Send Messages" permissions

2. **The bot works automatically**
   - When someone posts a message with x.com links
   - The bot replies with "Better embed:" and the stupidpenisx.com version
   - No manual intervention needed

## Commands

- `/start` - Show welcome message and instructions
- `/help` - Display help information
- `/status` - Check bot status

## Deployment

### Railway.app (Recommended)

1. Push your code to GitHub
2. Connect your Railway account to GitHub
3. Create a new project and select your repository
4. Add environment variable: `TELEGRAM_BOT_TOKEN`
5. Deploy automatically

### Render.com

1. Push your code to GitHub
2. Create a new Web Service on Render
3. Connect your GitHub repository
4. Set build command: `pip install -r requirements.txt`
5. Set start command: `python bot.py`
6. Add environment variable: `TELEGRAM_BOT_TOKEN`
7. Deploy

### Local Development

```bash
# Install dependencies
pip install -r requirements.txt

# Set environment variable
export TELEGRAM_BOT_TOKEN="your_bot_token"

# Run the bot
python bot.py
```

## Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `TELEGRAM_BOT_TOKEN` | Bot token from @BotFather | Yes |
| `WEBHOOK_URL` | Webhook URL for deployment | No |

### Logging

- Logs are saved to `logs/bot.log`
- Console output shows real-time activity
- Configurable log levels in `bot.py`

## Technical Details

### Supported URL Formats

The bot detects and processes:
- `https://x.com/username/status/123456`
- `https://twitter.com/username/status/123456`
- `http://x.com/username/status/123456`
- URLs with or without `www.`

### URL Replacement Logic

- `x.com` → `stupidpenisx.com`
- `twitter.com` → `stupidpenisx.com`
- Preserves all path parameters and fragments

### Security Features

- Input validation for all URLs
- Rate limiting protection
- Secure token handling via environment variables
- No sensitive data logging

## Troubleshooting

### Common Issues

**Bot doesn't respond:**
- Check if bot token is correct
- Ensure bot has "Read Messages" permission in the group
- Verify the bot is not muted or restricted

**Import errors:**
- Make sure all dependencies are installed: `pip install -r requirements.txt`
- Use Python 3.11+ as recommended

**Deployment issues:**
- Check environment variables are set correctly
- Ensure the hosting platform supports Python 3.11+
- Verify the start command is `python bot.py`

### Logs

Check `logs/bot.log` for detailed error information:

```bash
tail -f logs/bot.log
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source and available under the MIT License.

## Support

If you encounter any issues:
1. Check the troubleshooting section
2. Review the logs for error messages
3. Create an issue on GitHub with details

---

**Note:** This bot only processes messages containing x.com or twitter.com links. It doesn't store or log message content for privacy.
