#!/usr/bin/env python3
"""
Telegram X.com to StupidPenisX.com Link Replacer Bot

This bot monitors messages in groups/channels and replaces x.com links with stupidpenisx.com links
to provide better Twitter/X embeds.
"""

import logging
import os
import re
from datetime import datetime
from typing import List
from urllib.parse import urlparse
from threading import Thread
from http.server import HTTPServer, BaseHTTPRequestHandler
import time

from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
)
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    handlers=[
        logging.FileHandler('logs/bot.log', encoding='utf-8'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# URL detection pattern for x.com and twitter.com
URL_PATTERN = re.compile(
    r'https?://(?:www\.)?(?:twitter\.com|x\.com)/\S+',
    re.IGNORECASE
)

class HealthCheckHandler(BaseHTTPRequestHandler):
    """Simple health check handler for Render.com"""
    
    def do_GET(self):
        if self.path == '/health' or self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            
            health_data = {
                "status": "healthy",
                "service": "X.com to StupidPenisX.com Bot",
                "timestamp": datetime.now().isoformat(),
                "uptime": time.time() - start_time
            }
            
            self.wfile.write(str(health_data).encode())
        else:
            self.send_response(404)
            self.end_headers()
    
    def log_message(self, format, *args):
        # Suppress HTTP server logs
        pass

def start_health_server(port=10000):
    """Start health check server for Render.com"""
    try:
        server = HTTPServer(('0.0.0.0', port), HealthCheckHandler)
        logger.info(f"Health check server starting on port {port}")
        server.serve_forever()
    except Exception as e:
        logger.error(f"Health server error: {e}")

# Track start time for uptime calculation
start_time = time.time()

class XToStupidPenisXBot:
    """Main bot class for handling X.com to StupidPenisX.com link replacement"""
    
    def __init__(self, token: str):
        self.token = token
        self.application = None
        
    async def start_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Handle /start command"""
        start_message = (
            "🔄 X.com Link Replacer Bot 🔄\n\n"
            "I automatically replace x.com links with stupidpenisx.com links for better embeds!\n\n"
            "How it works:\n"
            "• Add me to your group or channel\n"
            "• Give me read and send message permissions\n"
            "• I'll automatically detect x.com links and reply with stupidpenisx.com versions\n\n"
            "Commands:\n"
            "/start - Show this help message\n"
            "/status - Check bot status\n"
            "/help - Show help information"
        )
        
        await update.message.reply_text(start_message)
        
        logger.info(f"Start command used by user {update.effective_user.id}")

    async def help_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Handle /help command"""
        help_message = (
            "🆘 Help - X.com Link Replacer Bot\n\n"
            "Purpose: Replace x.com links with stupidpenisx.com for better Twitter embeds\n\n"
            "Setup:\n"
            "1. Add the bot to your group/channel\n"
            "2. Grant read messages and send messages permissions\n"
            "3. The bot will automatically process messages with x.com links\n\n"
            "Supported Links:\n"
            "• x.com/username/status/123456\n"
            "• twitter.com/username/status/123456\n"
            "• Any x.com or twitter.com URL\n\n"
            "Privacy: The bot only processes messages containing x.com links"
        )
        
        await update.message.reply_text(help_message)
        
        logger.info(f"Help command used by user {update.effective_user.id}")

    async def status_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Handle /status command"""
        status_message = (
            "✅ Bot Status: Online\n\n"
            f"🕐 Current time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
            "🔄 Ready to process x.com links\n"
            "📊 All systems operational"
        )
        
        await update.message.reply_text(status_message)
        
        logger.info(f"Status command used by user {update.effective_user.id}")

    def extract_x_urls(self, text: str) -> List[str]:
        """Extract x.com and twitter.com URLs from text"""
        urls = URL_PATTERN.findall(text)
        return [url for url in urls if self.is_valid_twitter_url(url)]

    def is_valid_twitter_url(self, url: str) -> bool:
        """Validate if URL is a proper Twitter/X URL"""
        try:
            parsed = urlparse(url)
            domain = parsed.netloc.lower()
            
            # Check if it's a twitter.com or x.com domain
            valid_domains = ['twitter.com', 'www.twitter.com', 'x.com', 'www.x.com']
            
            return domain in valid_domains and parsed.path
        except Exception as e:
            logger.warning(f"Error validating URL {url}: {e}")
            return False

    def replace_with_stupidpenisx(self, url: str) -> str:
        """Replace x.com or twitter.com with stupidpenisx.com"""
        # Replace twitter.com with stupidpenisx.com
        if 'twitter.com' in url:
            return url.replace('twitter.com', 'stupidpenisx.com')
        
        # Replace x.com with stupidpenisx.com
        if 'x.com' in url:
            return url.replace('x.com', 'stupidpenisx.com')
        
        return url

    async def handle_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Handle incoming messages and process x.com links"""
        try:
            # Skip if no message text
            if not update.message or not update.message.text:
                return

            message_text = update.message.text
            chat_type = update.effective_chat.type
            user_id = update.effective_user.id if update.effective_user else "Unknown"
            
            # Extract x.com/twitter.com URLs
            x_urls = self.extract_x_urls(message_text)
            
            if not x_urls:
                return  # No x.com links found
            
            logger.info(f"Found {len(x_urls)} x.com links in message from user {user_id} in {chat_type}")
            
            # Replace URLs with stupidpenisx.com versions
            stupidpenisx_urls = [self.replace_with_stupidpenisx(url) for url in x_urls]
            
            # Create response message
            if len(stupidpenisx_urls) == 1:
                response = f"🔄 Краще видно:\n{stupidpenisx_urls[0]}"
            else:
                response = "🔄 Краще видно:\n" + "\n".join(stupidpenisx_urls)
            
            # Reply to the original message
            await update.message.reply_text(
                response,
                disable_web_page_preview=False
            )
            
            logger.info(f"Successfully replied with {len(stupidpenisx_urls)} stupidpenisx.com links")
            
        except Exception as e:
            logger.error(f"Error handling message: {e}")
            # Don't send error messages to users to avoid spam

    async def error_handler(self, update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Handle errors"""
        logger.error(f"Exception while handling an update: {context.error}")

    def run(self):
        """Run the bot"""
        try:
            # Create application
            self.application = Application.builder().token(self.token).build()
            
            # Add handlers
            self.application.add_handler(CommandHandler("start", self.start_command))
            self.application.add_handler(CommandHandler("help", self.help_command))
            self.application.add_handler(CommandHandler("status", self.status_command))
            
            # Message handler for all text messages
            self.application.add_handler(
                MessageHandler(filters.TEXT & ~filters.COMMAND, self.handle_message)
            )
            
            # Error handler
            self.application.add_error_handler(self.error_handler)
            
            logger.info("Bot starting...")
            
            # Start health check server in background thread for Render.com
            port = int(os.getenv('PORT', 10000))
            health_thread = Thread(target=start_health_server, args=(port,), daemon=True)
            health_thread.start()
            
            # Run the bot
            self.application.run_polling(
                allowed_updates=Update.ALL_TYPES,
                drop_pending_updates=True
            )
            
        except Exception as e:
            logger.error(f"Error starting bot: {e}")
            raise

def main():
    """Main function"""
    # Create logs directory if it doesn't exist
    os.makedirs('logs', exist_ok=True)
    
    # Get bot token from environment
    bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
    
    if not bot_token:
        logger.error("TELEGRAM_BOT_TOKEN environment variable not found!")
        print("❌ Error: TELEGRAM_BOT_TOKEN environment variable not found!")
        print("Please set your bot token in the .env file or environment variables.")
        return
    
    # Create and run bot
    bot = XToStupidPenisXBot(bot_token)
    
    try:
        logger.info("Starting X.com to StupidPenisX.com Link Replacer Bot...")
        print("🚀 Starting X.com to StupidPenisX.com Link Replacer Bot...")
        print("Press Ctrl+C to stop the bot")
        
        bot.run()
        
    except KeyboardInterrupt:
        logger.info("Bot stopped by user")
        print("\n🛑 Bot stopped by user")
    except Exception as e:
        logger.error(f"Fatal error: {e}")
        print(f"❌ Fatal error: {e}")

if __name__ == '__main__':
    main()
