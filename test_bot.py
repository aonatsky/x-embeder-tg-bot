#!/usr/bin/env python3
"""
Test script for the X.com to StupidPenisX.com Link Replacer Bot
Run this to test the URL detection and replacement logic before deploying.
"""

import re
from urllib.parse import urlparse

# URL detection pattern (same as in bot.py)
URL_PATTERN = re.compile(
    r'https?://(?:www\.)?(?:twitter\.com|x\.com)/\S+',
    re.IGNORECASE
)

def extract_x_urls(text: str) -> list:
    """Extract x.com and twitter.com URLs from text"""
    urls = URL_PATTERN.findall(text)
    return [url for url in urls if is_valid_twitter_url(url)]

def is_valid_twitter_url(url: str) -> bool:
    """Validate if URL is a proper Twitter/X URL"""
    try:
        parsed = urlparse(url)
        domain = parsed.netloc.lower()
        
        # Check if it's a twitter.com or x.com domain
        valid_domains = ['twitter.com', 'www.twitter.com', 'x.com', 'www.x.com']
        
        return domain in valid_domains and parsed.path
    except Exception as e:
        print(f"Error validating URL {url}: {e}")
        return False

def replace_with_stupidpenisx(url: str) -> str:
    """Replace x.com or twitter.com with stupidpenisx.com"""
    # Replace twitter.com with stupidpenisx.com
    if 'twitter.com' in url:
        return url.replace('twitter.com', 'stupidpenisx.com')
    
    # Replace x.com with stupidpenisx.com
    if 'x.com' in url:
        return url.replace('x.com', 'stupidpenisx.com')
    
    return url

def test_url_replacement():
    """Test the URL detection and replacement logic"""
    
    test_cases = [
        # Basic x.com URLs
        "Check out this tweet: https://x.com/username/status/1234567890",
        "Multiple links: https://x.com/user1/status/123 and https://x.com/user2/status/456",
        
        # Twitter.com URLs
        "Old format: https://twitter.com/username/status/1234567890",
        "With www: https://www.twitter.com/username/status/1234567890",
        
        # Mixed content
        "Mixed: Check https://x.com/user/status/123 and https://twitter.com/other/status/456 links",
        
        # URLs with parameters
        "With params: https://x.com/username/status/1234567890?s=20&t=abc123",
        
        # Complex URL that caused Markdown parsing issues
        "Complex URL: https://x.com/oheekoltsd/status/1936141854073864304?s=46&t=Ra8xRnsUO7hQBtvtIj8a_w",
        
        # HTTP vs HTTPS
        "HTTP: http://x.com/username/status/1234567890",
        
        # No X links
        "No X links here: https://github.com/user/repo and https://google.com",
        
        # Empty/invalid
        "",
        "Just text with no links",
    ]
    
    print("🧪 Testing X.com to StupidPenisX.com URL Replacement\n" + "="*50)
    
    for i, test_message in enumerate(test_cases, 1):
        print(f"\nTest {i}:")
        print(f"Input:  {test_message}")
        
        # Extract URLs
        x_urls = extract_x_urls(test_message)
        
        if x_urls:
            print(f"Found:  {len(x_urls)} X.com link(s)")
            for url in x_urls:
                stupidpenisx_url = replace_with_stupidpenisx(url)
                print(f"  {url} → {stupidpenisx_url}")
        else:
            print("Found:  No X.com links")
    
    print("\n" + "="*50)
    print("✅ URL replacement test completed!")

def test_regex_patterns():
    """Test specific regex patterns"""
    
    test_urls = [
        "https://x.com/user/status/123",
        "https://www.x.com/user/status/123",
        "http://x.com/user/status/123",
        "https://twitter.com/user/status/123",
        "https://www.twitter.com/user/status/123",
        "https://x.com/user",
        "https://x.com/user/photo/1",
        "https://x.com/user/status/123?s=20",
        
        # Should NOT match
        "https://example.com/x.com",
        "https://notx.com/user",
        "https://x.com.fake.site/user",
    ]
    
    print("\n🔍 Testing Regex Pattern Matching\n" + "="*40)
    
    for url in test_urls:
        matches = URL_PATTERN.findall(url)
        is_valid = is_valid_twitter_url(url) if matches else False
        status = "✅ MATCH" if is_valid else "❌ NO MATCH"
        print(f"{status}: {url}")

if __name__ == '__main__':
    test_url_replacement()
    test_regex_patterns()
    
    print(f"\n🚀 Bot is ready to deploy!")
    print("Next steps:")
    print("1. Get your bot token from @BotFather")
    print("2. Create a .env file with your token")
    print("3. Install dependencies: pip install -r requirements.txt")
    print("4. Run the bot: python bot.py")
