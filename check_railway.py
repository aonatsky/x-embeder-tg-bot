#!/usr/bin/env python3
"""
Railway Deployment Checker
Quick verification that your bot is ready for Railway.app deployment
"""

import os
import subprocess
import sys

def check_railway_requirements():
    """Check Railway-specific requirements"""
    print("🚂 Railway.app Deployment Check")
    print("=" * 35)
    
    checks = []
    
    # Check for required files
    print("📋 Checking required files...")
    required_files = ['bot.py', 'requirements.txt', 'railway.toml']
    
    for file in required_files:
        if os.path.exists(file):
            print(f"✅ {file}")
            checks.append(True)
        else:
            print(f"❌ {file} - MISSING")
            checks.append(False)
    
    # Check git status
    print("\n📁 Checking git repository...")
    try:
        result = subprocess.run(['git', 'status', '--porcelain'], 
                              capture_output=True, text=True)
        
        if result.returncode == 0:
            if result.stdout.strip():
                print("⚠️  Uncommitted changes detected")
                print("   Run: git add . && git commit -m 'Ready for Railway'")
            else:
                print("✅ No uncommitted changes")
            
            # Check for remote
            remote_result = subprocess.run(['git', 'remote', '-v'], 
                                         capture_output=True, text=True)
            if 'github.com' in remote_result.stdout:
                print("✅ GitHub remote configured")
                checks.append(True)
            else:
                print("❌ No GitHub remote found")
                print("   Railway needs your code on GitHub")
                checks.append(False)
        else:
            print("❌ Not a git repository")
            checks.append(False)
            
    except FileNotFoundError:
        print("❌ Git not installed")
        checks.append(False)
    
    # Check requirements.txt
    print("\n📦 Checking dependencies...")
    if os.path.exists('requirements.txt'):
        with open('requirements.txt', 'r') as f:
            content = f.read()
        
        if 'python-telegram-bot' in content:
            print("✅ python-telegram-bot found")
            checks.append(True)
        else:
            print("❌ python-telegram-bot missing from requirements.txt")
            checks.append(False)
    else:
        print("❌ requirements.txt not found")
        checks.append(False)
    
    return all(checks)

def show_railway_steps():
    """Show Railway deployment steps"""
    print("\n🚀 Railway Deployment Steps:")
    print("=" * 30)
    print("1. 🌐 Go to railway.app and sign up with GitHub")
    print("2. ➕ Click 'New Project' → 'Deploy from GitHub repo'")
    print("3. 📁 Select your 'x-embeder-tg-bot' repository")
    print("4. 🔧 Add environment variable:")
    print("   • Name: TELEGRAM_BOT_TOKEN")
    print("   • Value: Your bot token from @BotFather")
    print("5. 🚀 Deploy!")
    print("\n⏱️  Deployment usually takes 1-2 minutes")
    print("📖 See DEPLOY_RAILWAY.md for detailed guide")

def check_bot_token_reminder():
    """Remind about bot token"""
    print("\n🤖 Bot Token Reminder:")
    print("=" * 22)
    print("📱 Don't have a bot token yet?")
    print("1. Message @BotFather on Telegram")
    print("2. Send: /newbot")
    print("3. Follow the setup instructions")
    print("4. Copy your token (format: 123456:ABC-DEF...)")
    print("5. Add it to Railway environment variables")

def main():
    """Main function"""
    if check_railway_requirements():
        print("\n✅ All checks passed! Ready for Railway deployment")
        show_railway_steps()
        check_bot_token_reminder()
        
        print(f"\n🎯 Next: Deploy at railway.app")
        return 0
    else:
        print("\n❌ Some checks failed. Please fix issues before deploying")
        return 1

if __name__ == '__main__':
    sys.exit(main())
