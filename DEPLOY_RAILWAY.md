# Deploying to Railway.app - Complete Guide

## Why Railway.app?
- ✅ **Easy deployment** from GitHub
- ✅ **Free tier** with generous limits
- ✅ **Automatic builds** and deployments
- ✅ **Built-in environment variables**
- ✅ **No sleeping** (unlike some other free services)
- ✅ **Great for Telegram bots**

## Prerequisites
- ✅ Your code is on GitHub (already done!)
- ✅ You have a Telegram bot token from @BotFather
- ✅ Railway.app account (free signup)

## Step 1: Get Your Bot Token

If you don't have one yet:

1. Open Telegram and search for **@BotFather**
2. Start a chat and send: `/newbot`
3. Choose a name: `X Link Replacer Bot`
4. Choose a username: `xlinkembeder_bot` (or similar)
5. **Copy the bot token** (looks like: `1234567890:ABCDefGhIJKlMnOpQrStUvWxYz`)

## Step 2: Deploy to Railway

### 2.1 Create Railway Account
1. Go to [railway.app](https://railway.app)
2. Click **"Login"** and sign up with GitHub
3. Authorize Railway to access your GitHub repositories

### 2.2 Create New Project
1. Click **"New Project"**
2. Select **"Deploy from GitHub repo"**
3. Find and select your `x-embeder-tg-bot` repository
4. Click **"Deploy Now"**

### 2.3 Configure Environment Variables
1. In your Railway dashboard, click on your deployed service
2. Go to **"Variables"** tab
3. Click **"New Variable"**
4. Add:
   - **Name**: `TELEGRAM_BOT_TOKEN`
   - **Value**: Your bot token from @BotFather
5. Click **"Add"**

### 2.4 Monitor Deployment
1. Go to **"Deployments"** tab
2. Watch the build process (usually takes 1-2 minutes)
3. Look for successful deployment status

## Step 3: Verify Your Bot is Working

### 3.1 Check Logs
1. In Railway dashboard, go to **"Deployments"** tab
2. Click on your latest deployment
3. Look for logs showing:
   ```
   🚀 Starting X.com to StupidPenisX.com Link Replacer Bot...
   Bot starting...
   ```

### 3.2 Test Your Bot
1. **Add bot to a Telegram group**:
   - Search for your bot username in Telegram
   - Add it to a test group
   - Make it an admin with "Delete Messages" and "Send Messages" permissions

2. **Test the functionality**:
   - Send: `Check this out: https://x.com/username/status/123456`
   - Your bot should reply: `🔄 Better embed: https://stupidpenisx.com/username/status/123456`

## Step 4: Enable Auto-Deploy (Recommended)

Railway automatically redeploys when you push to GitHub:

1. Make any change to your code
2. Commit and push:
   ```fish
   git add .
   git commit -m "Update bot"
   git push
   ```
3. Railway will automatically rebuild and deploy

## Troubleshooting

### Common Issues:

**❌ Build Failed**
- Check Railway build logs in "Deployments" tab
- Ensure `requirements.txt` is present and valid
- Verify `runtime.txt` specifies correct Python version

**❌ Bot Not Starting**
- Verify `TELEGRAM_BOT_TOKEN` environment variable is set
- Check logs for Python errors
- Ensure bot token is valid (test with @BotFather)

**❌ Bot Not Responding**
- Make sure bot is added to groups with proper permissions
- Test with `/start` command in private chat first
- Check Railway logs for runtime errors

**❌ "Module not found" errors**
- Verify all dependencies are in `requirements.txt`
- Check that virtual environment isn't committed to GitHub

### Debug Commands:

**Check Railway logs:**
```fish
# Install Railway CLI (optional)
npm install -g @railway/cli
railway login
railway logs
```

**Local testing:**
```fish
# Test locally before deploying
source venv/bin/activate  # or: . venv/bin/activate.fish
python bot.py
```

## Railway.app Features

### Free Tier Includes:
- ✅ **$5 worth of usage per month** (plenty for a bot)
- ✅ **512MB RAM, 1GB storage**
- ✅ **No sleeping** (bot runs 24/7)
- ✅ **Custom domains**
- ✅ **Automatic HTTPS**

### Monitoring:
- **Usage Dashboard**: Track resource consumption
- **Deployment History**: See all deployments
- **Real-time Logs**: Monitor bot activity
- **Metrics**: CPU, memory, network usage

## Advanced Configuration

### Custom Start Command (if needed):
If you need to customize how your bot starts, modify `railway.toml`:

```toml
[deploy]
startCommand = "python -u bot.py"  # -u for unbuffered output
```

### Environment Variables Best Practices:
- Never commit sensitive tokens to GitHub
- Use Railway's environment variables for all secrets
- Consider adding `PORT` if you add webhook support later

## Security & Best Practices

- ✅ **Environment Variables**: All secrets stored securely in Railway
- ✅ **GitHub Integration**: Code stays in your repository
- ✅ **Automatic Updates**: Push to deploy
- ✅ **Monitoring**: Built-in logs and metrics

## Scaling (If Needed Later)

Railway makes it easy to scale:
- **Upgrade Plan**: More resources available
- **Add Databases**: PostgreSQL, Redis, etc.
- **Custom Domains**: Your own domain name
- **Team Collaboration**: Share projects

---

## 🎉 Your Bot is Now Live on Railway!

### What happens next:
1. ✅ Your bot runs 24/7 on Railway's infrastructure
2. ✅ Automatically processes x.com links in Telegram groups
3. ✅ Updates deploy automatically when you push to GitHub
4. ✅ Built-in monitoring and logging

### Example Bot Behavior:
- **User posts**: `https://x.com/elonmusk/status/123456`
- **Bot replies**: `🔄 Better embed: https://stupidpenisx.com/elonmusk/status/123456`

### Useful Links:
- **Railway Dashboard**: [railway.app/dashboard](https://railway.app/dashboard)
- **Your Bot**: Search for your bot username in Telegram
- **Logs**: Check deployment logs in Railway dashboard

Need help? Railway has excellent documentation and community support!
