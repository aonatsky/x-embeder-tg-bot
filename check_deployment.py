#!/usr/bin/env python3
"""
Pre-deployment checker for Render.com
This script helps ensure your bot is ready for deployment
"""

import os
import sys
import subprocess

def check_files():
    """Check if required files exist"""
    print("📋 Checking required files...")
    
    required_files = [
        'bot.py',
        'requirements.txt',
        '.env.example',
        'README.md'
    ]
    
    missing_files = []
    for file in required_files:
        if os.path.exists(file):
            print(f"✅ {file}")
        else:
            print(f"❌ {file} - MISSING")
            missing_files.append(file)
    
    return len(missing_files) == 0

def check_env_file():
    """Check .env file configuration"""
    print("\n🔑 Checking environment configuration...")
    
    if os.path.exists('.env'):
        with open('.env', 'r') as f:
            content = f.read()
            
        if 'your_bot_token_here' in content:
            print("⚠️  .env file contains placeholder token")
            print("   You'll need to set TELEGRAM_BOT_TOKEN in Render dashboard")
        elif 'TELEGRAM_BOT_TOKEN=' in content:
            print("✅ .env file configured (will use Render environment variables)")
        else:
            print("❌ .env file missing TELEGRAM_BOT_TOKEN")
            return False
    else:
        print("✅ No .env file (will use Render environment variables)")
    
    return True

def check_requirements():
    """Check requirements.txt"""
    print("\n📦 Checking requirements.txt...")
    
    if not os.path.exists('requirements.txt'):
        print("❌ requirements.txt not found")
        return False
    
    with open('requirements.txt', 'r') as f:
        content = f.read()
    
    required_packages = ['python-telegram-bot', 'python-dotenv']
    
    for package in required_packages:
        if package in content:
            print(f"✅ {package}")
        else:
            print(f"❌ {package} - MISSING")
            return False
    
    return True

def check_git_status():
    """Check git status"""
    print("\n📁 Checking git status...")
    
    try:
        # Check if git is initialized
        result = subprocess.run(['git', 'status'], 
                              capture_output=True, text=True, cwd='.')
        
        if result.returncode != 0:
            print("❌ Git not initialized")
            print("   Run: git init")
            return False
        
        # Check for uncommitted changes
        if 'nothing to commit' in result.stdout:
            print("✅ No uncommitted changes")
        else:
            print("⚠️  You have uncommitted changes")
            print("   Run: git add . && git commit -m 'Ready for deployment'")
        
        # Check for remote
        remote_result = subprocess.run(['git', 'remote', '-v'], 
                                     capture_output=True, text=True, cwd='.')
        
        if remote_result.stdout:
            print("✅ Git remote configured")
        else:
            print("⚠️  No git remote configured")
            print("   Add your GitHub repo: git remote add origin <your-repo-url>")
        
        return True
        
    except FileNotFoundError:
        print("❌ Git not installed")
        return False

def show_deployment_summary():
    """Show deployment summary"""
    print("\n🚀 Render.com Deployment Summary:")
    print("=" * 50)
    print("1. Push your code to GitHub")
    print("2. Go to render.com and create account")
    print("3. Create new Web Service")
    print("4. Connect your GitHub repository")
    print("5. Configure settings:")
    print("   - Build Command: pip install -r requirements.txt")
    print("   - Start Command: python bot.py") 
    print("   - Environment Variable: TELEGRAM_BOT_TOKEN=<your-token>")
    print("6. Deploy!")
    print("\n📖 See DEPLOY_RENDER.md for detailed instructions")

def main():
    """Main function"""
    print("🔍 Pre-Deployment Check for Render.com")
    print("=" * 45)
    
    checks = [
        check_files(),
        check_env_file(),
        check_requirements(),
        check_git_status()
    ]
    
    print("\n" + "=" * 45)
    
    if all(checks):
        print("✅ All checks passed! Ready for deployment")
        show_deployment_summary()
    else:
        print("❌ Some checks failed. Please fix issues before deploying")
        return 1
    
    return 0

if __name__ == '__main__':
    sys.exit(main())
