# Deploying to Render.com - Step by Step Guide

## Prerequisites
- Your bot is working locally (optional but recommended for testing)
- You have a GitHub account
- You have a Render.com account (free signup available)
- You have a Telegram bot token from @BotFather

## Step 1: Prepare Your Code for Deployment

### 1.1 Push to GitHub
First, make sure your code is on GitHub:

```bash
# Initialize git (if not already done)
git init

# Add all files
git add .

# Commit your changes
git commit -m "Initial commit: X.com to StupidPenisX.com bot"

# Add your GitHub repository
git remote add origin https://github.com/yourusername/x-embeder-tg-bot.git

# Push to GitHub
git push -u origin main
```

## Step 2: Deploy on Render.com

### 2.1 Create Render Account
1. Go to [render.com](https://render.com)
2. Sign up for a free account
3. Verify your email address

### 2.2 Create New Web Service
1. Click **"New +"** button in your Render dashboard
2. Select **"Web Service"**
3. Choose **"Build and deploy from a Git repository"**
4. Click **"Connect to GitHub"** and authorize Render

### 2.3 Configure Repository
1. Find your `x-embeder-tg-bot` repository
2. Click **"Connect"**

### 2.4 Configure Service Settings
Fill in these settings:

**Basic Settings:**
- **Name**: `x-embeder-tg-bot` (or your preferred name)
- **Region**: Choose closest to your users
- **Branch**: `main` (or your default branch)
- **Runtime**: `Python 3`

**Build & Deploy:**
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `python bot.py`

**Advanced Settings:**
- **Instance Type**: `Free` (for testing) or `Starter` (for production)
- **Auto-Deploy**: `Yes` (recommended)

## Step 3: Set Environment Variables

### 3.1 Add Bot Token
1. In your service settings, go to **"Environment"** tab
2. Click **"Add Environment Variable"**
3. Add:
   - **Key**: `TELEGRAM_BOT_TOKEN`
   - **Value**: Your bot token from @BotFather (e.g., `1234567890:ABCDefGhIJKlMnOpQrStUvWxYz`)

### 3.2 Optional: Add Python Version
1. Add another environment variable:
   - **Key**: `PYTHON_VERSION`
   - **Value**: `3.11.0`

## Step 4: Deploy

1. Click **"Create Web Service"**
2. Render will start building your application
3. Wait for the build to complete (usually 2-5 minutes)
4. Your bot should start automatically

## Step 5: Verify Deployment

### 5.1 Check Logs
1. Go to your service dashboard
2. Click on **"Logs"** tab
3. Look for messages like:
   ```
   🚀 Starting X.com to StupidPenisX.com Link Replacer Bot...
   Bot starting...
   ```

### 5.2 Test Your Bot
1. Add your bot to a Telegram group
2. Send a message with an x.com link
3. Verify the bot replies with stupidpenisx.com version

## Troubleshooting

### Common Issues:

**❌ Build Failed:**
- Check that `requirements.txt` exists
- Verify Python syntax in `bot.py`
- Check build logs for specific errors

**❌ Bot Not Starting:**
- Verify `TELEGRAM_BOT_TOKEN` is set correctly
- Check that token has no extra spaces
- Ensure bot token is valid

**❌ Bot Not Responding:**
- Verify bot is added to groups with proper permissions
- Check that bot has "Read Messages" permission
- Test with /start command in private chat first

### Useful Commands for Debugging:
1. **View Recent Logs**: Check the Logs tab in Render dashboard
2. **Restart Service**: Use "Manual Deploy" button
3. **Check Environment Variables**: Verify in Environment tab

## Free Tier Limitations

Render.com free tier includes:
- ✅ 750 hours per month (enough for 24/7 operation)
- ✅ Automatic SSL certificates
- ✅ Custom domains (optional)
- ⚠️ Services may sleep after 15 minutes of inactivity
- ⚠️ Cold start delay when waking up

For production use, consider upgrading to Starter plan ($7/month) for:
- No sleeping
- Better performance
- More resources

## Alternative: Environment File Method

If you prefer to keep your token in a file:

1. Create `.env` file locally with your token
2. **DO NOT** commit `.env` to GitHub
3. Set environment variables through Render dashboard instead

## Security Best Practices

- ✅ Never commit your bot token to GitHub
- ✅ Use environment variables for sensitive data
- ✅ Regularly rotate your bot token if needed
- ✅ Monitor bot logs for unusual activity

## Monitoring Your Bot

1. **Render Dashboard**: Check service status and logs
2. **Telegram**: Monitor bot responses in your groups
3. **Bot Commands**: Use `/status` command to check bot health

---

## 🎉 Your Bot is Live!

Once deployed successfully:
1. Your bot runs 24/7 on Render's servers
2. It automatically processes x.com links in Telegram groups
3. Updates are deployed automatically when you push to GitHub
4. You can monitor performance through Render dashboard

Need help? Check the troubleshooting section or Render's documentation!
