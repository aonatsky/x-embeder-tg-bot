# Fixing Render.com Deployment Issue

## Problem
Your bot is getting a "Port scan timeout" error because Render.com expects web services to bind to a port and serve HTTP requests, but Telegram bots typically use polling instead.

## Solution
I've updated your bot to include a health check endpoint that satisfies Render.com's requirements.

## What Changed
1. **Added Health Check Server**: Your bot now runs a simple HTTP server on the port Render expects
2. **Background Threading**: The bot runs in the background while serving HTTP health checks
3. **Updated Configuration**: render.yaml now includes proper health check configuration

## How to Fix Your Current Deployment

### Option 1: Update Your Existing Service (Recommended)

1. **Commit the changes**:
   ```bash
   git add .
   git commit -m "Add health check endpoint for Render.com"
   git push
   ```

2. **Redeploy on Render**:
   - Go to your Render dashboard
   - Find your failed service
   - Click "Manual Deploy" to trigger a new deployment
   - The new code will include the health check endpoint

### Option 2: Create a Background Worker Instead

If you prefer a cleaner approach:

1. **Delete the current service** on Render.com
2. **Create a new "Background Worker"** instead of "Web Service":
   - Go to Render dashboard
   - Click "New +" → "Background Worker"
   - Select your repository
   - Set start command: `python bot.py`
   - Add environment variable: `TELEGRAM_BOT_TOKEN`

Background workers don't need to bind to ports, so they're perfect for Telegram bots.

## Recommended Approach: Background Worker

Since your bot doesn't need to serve web traffic, a background worker is more appropriate:

### Steps for Background Worker:
1. **Delete current web service** (if it exists)
2. **Create Background Worker**:
   - Type: Background Worker
   - Repository: x-embeder-tg-bot
   - Start Command: `python bot.py`
   - Environment Variables:
     - `TELEGRAM_BOT_TOKEN`: Your bot token

### Benefits of Background Worker:
- ✅ No port binding required
- ✅ Simpler configuration
- ✅ Better for long-running bots
- ✅ Uses fewer resources

## Testing the Fix

Once deployed (either way), test your bot:

1. **Check Logs**: Look for "🚀 Starting X.com to StupidPenisX.com Link Replacer Bot..."
2. **Test Bot**: Send a message with an x.com link in a Telegram group
3. **Verify Response**: Bot should reply with stupidpenisx.com version

## Health Check Endpoint

If you keep the web service, you can check the health endpoint:
- URL: `https://your-app-name.onrender.com/health`
- Should return bot status and uptime

## Next Steps

Choose your preferred option:
- **Quick Fix**: Push the updated code and redeploy
- **Clean Approach**: Delete service and create background worker

Both will work, but background worker is more appropriate for Telegram bots.

---

**Need help?** The updated bot code now works with both approaches!
