#!/usr/bin/env python3
"""
Example script showing how to configure and test the bot locally
"""

import os

def show_env_example():
    """Show example .env configuration"""
    print("📝 Example .env file configuration:")
    print("=" * 40)
    print("# Telegram Bot Configuration")
    print("TELEGRAM_BOT_TOKEN=1234567890:ABCDefGhIJKlMnOpQrStUvWxYz1234567890")
    print("")
    print("# Optional: For webhook deployment (Railway/Render)")
    print("# WEBHOOK_URL=https://your-app.railway.app/webhook")
    print("=" * 40)

def show_bot_father_steps():
    """Show steps to create a bot with BotFather"""
    print("\n🤖 Creating a bot with @BotFather:")
    print("=" * 40)
    print("1. Open Telegram and search for @BotFather")
    print("2. Start a chat with @BotFather")
    print("3. Send: /newbot")
    print("4. Choose a name for your bot (e.g., 'X Link Replacer Bot')")
    print("5. Choose a username ending in 'bot' (e.g., 'xlinkembeder_bot')")
    print("6. Copy the token that BotFather gives you")
    print("7. Paste it in your .env file")
    print("=" * 40)

def show_deployment_options():
    """Show deployment options"""
    print("\n☁️  Deployment Options:")
    print("=" * 40)
    print("🚀 Railway.app (Recommended):")
    print("   1. Push code to GitHub")
    print("   2. Connect Railway to your GitHub repo")
    print("   3. Add TELEGRAM_BOT_TOKEN environment variable")
    print("   4. Deploy automatically")
    print("")
    print("🔷 Render.com:")
    print("   1. Push code to GitHub")
    print("   2. Create new Web Service on Render")
    print("   3. Set start command: python bot.py")
    print("   4. Add TELEGRAM_BOT_TOKEN environment variable")
    print("   5. Deploy")
    print("")
    print("💻 Local Development:")
    print("   1. source venv/bin/activate")
    print("   2. python bot.py")
    print("=" * 40)

def show_usage_examples():
    """Show usage examples"""
    print("\n💡 Bot Usage Examples:")
    print("=" * 40)
    print("When someone posts these messages in a group:")
    print("")
    print("📥 Input:  'Check out this tweet: https://x.com/username/status/123456'")
    print("📤 Output: '🔄 Better embed: https://stupidpenisx.com/username/status/123456'")
    print("")
    print("📥 Input:  'Multiple: https://x.com/user1/status/123 https://twitter.com/user2/status/456'")
    print("📤 Output: '🔄 Better embeds:")
    print("           https://stupidpenisx.com/user1/status/123")
    print("           https://stupidpenisx.com/user2/status/456'")
    print("=" * 40)

def show_troubleshooting():
    """Show common troubleshooting tips"""
    print("\n🔧 Troubleshooting:")
    print("=" * 40)
    print("❌ Bot doesn't respond:")
    print("   • Check bot token is correct in .env")
    print("   • Ensure bot has 'Read Messages' permission")
    print("   • Make sure bot isn't muted in the group")
    print("")
    print("❌ Import errors:")
    print("   • Run: source venv/bin/activate")
    print("   • Run: pip install -r requirements.txt")
    print("")
    print("❌ Deployment issues:")
    print("   • Check environment variables are set")
    print("   • Verify Python 3.11+ is used")
    print("   • Check logs for detailed errors")
    print("=" * 40)

def main():
    """Main demo function"""
    print("🔄 X.com to StupidPenisX.com Link Replacer Bot")
    print("Complete Setup & Configuration Guide")
    print("=" * 50)
    
    show_env_example()
    show_bot_father_steps()
    show_deployment_options()
    show_usage_examples()
    show_troubleshooting()
    
    print(f"\n✅ Setup is complete! Your bot is ready to use.")
    print(f"📁 Project location: {os.getcwd()}")
    print(f"🔧 To start: source venv/bin/activate && python bot.py")

if __name__ == '__main__':
    main()
