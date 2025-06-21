#!/usr/bin/env python3
"""
Setup script for X.com to FX.com Link Replacer Bot
Run this script to set up your bot quickly.
"""

import os
import sys
import subprocess

def check_python_version():
    """Check if Python version is 3.11+"""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 11):
        print("❌ Python 3.11 or higher is required")
        print(f"Current version: {version.major}.{version.minor}")
        return False
    
    print(f"✅ Python version: {version.major}.{version.minor}")
    return True

def create_virtual_environment():
    """Create a virtual environment"""
    print("\n📦 Setting up virtual environment...")
    
    try:
        subprocess.run([sys.executable, "-m", "venv", "venv"], check=True)
        print("✅ Virtual environment created")
        
        # Determine the activation script path
        if os.name == 'nt':  # Windows
            activate_path = "venv\\Scripts\\activate"
        else:  # Unix/Linux/macOS
            activate_path = "venv/bin/activate"
        
        print(f"To activate: source {activate_path}")
        return True
        
    except subprocess.CalledProcessError:
        print("❌ Failed to create virtual environment")
        return False

def install_dependencies():
    """Install required dependencies"""
    print("\n📚 Installing dependencies...")
    
    try:
        # Use the virtual environment's pip if it exists
        if os.path.exists("venv"):
            if os.name == 'nt':  # Windows
                pip_path = "venv\\Scripts\\pip"
            else:  # Unix/Linux/macOS
                pip_path = "venv/bin/pip"
        else:
            pip_path = "pip"
        
        subprocess.run([pip_path, "install", "-r", "requirements.txt"], check=True)
        print("✅ Dependencies installed successfully")
        return True
        
    except subprocess.CalledProcessError:
        print("❌ Failed to install dependencies")
        print("Try running manually: pip install -r requirements.txt")
        return False

def setup_environment_file():
    """Help user set up the .env file"""
    print("\n⚙️  Setting up environment file...")
    
    if os.path.exists(".env"):
        print("✅ .env file already exists")
        return True
    
    if not os.path.exists(".env.example"):
        print("❌ .env.example file not found")
        return False
    
    # Copy .env.example to .env
    try:
        with open(".env.example", "r") as source:
            content = source.read()
        
        with open(".env", "w") as target:
            target.write(content)
        
        print("✅ .env file created from template")
        print("\n🔑 IMPORTANT: You need to add your bot token to the .env file!")
        print("1. Get your bot token from @BotFather on Telegram")
        print("2. Edit .env file and replace 'your_bot_token_here' with your actual token")
        
        return True
        
    except Exception as e:
        print(f"❌ Failed to create .env file: {e}")
        return False

def run_tests():
    """Run the test script to verify setup"""
    print("\n🧪 Running tests...")
    
    try:
        subprocess.run([sys.executable, "test_bot.py"], check=True)
        return True
    except subprocess.CalledProcessError:
        print("❌ Tests failed")
        return False

def main():
    """Main setup function"""
    print("🚀 X.com to FX.com Link Replacer Bot Setup")
    print("=" * 45)
    
    # Check Python version
    if not check_python_version():
        return False
    
    # Create virtual environment
    if not create_virtual_environment():
        print("⚠️  Continuing without virtual environment...")
    
    # Install dependencies
    if not install_dependencies():
        return False
    
    # Setup environment file
    if not setup_environment_file():
        return False
    
    # Run tests
    if not run_tests():
        print("⚠️  Tests failed, but setup may still work")
    
    print("\n✅ Setup completed successfully!")
    print("\n📋 Next steps:")
    print("1. Get your bot token from @BotFather on Telegram:")
    print("   - Message @BotFather")
    print("   - Use /newbot command")
    print("   - Follow the instructions")
    print("   - Copy your bot token")
    print()
    print("2. Edit the .env file and add your bot token")
    print()
    print("3. Run the bot:")
    if os.path.exists("venv"):
        if os.name == 'nt':  # Windows
            print("   venv\\Scripts\\python bot.py")
        else:  # Unix/Linux/macOS
            print("   source venv/bin/activate")
            print("   python bot.py")
    else:
        print("   python bot.py")
    print()
    print("4. Add your bot to Telegram groups/channels")
    print("5. Give it read and send message permissions")
    print()
    print("🎉 Your bot will automatically replace x.com links with fx.com!")

if __name__ == '__main__':
    main()
