# Changelog

## v1.1.0 - 2025-06-21

### Changed
- **Breaking Change**: Updated URL replacement from `fx.com` to `stupidpenisx.com`
- All x.com links now redirect to stupidpenisx.com instead of fx.com
- All twitter.com links now redirect to stupidpenisx.com instead of fx.com

### Updated Files
- `bot.py` - Main bot logic updated to use stupidpenisx.com
- `test_bot.py` - Test cases updated to reflect new replacement logic
- `README.md` - Documentation updated with new service name
- `PROJECT_SUMMARY.md` - Project summary updated
- `package.json` - Package description and keywords updated
- `demo.py` - Demo examples updated

### Technical Details
- Class renamed from `XToFXBot` to `XToStupidPenisXBot`
- Function renamed from `replace_with_fx()` to `replace_with_stupidpenisx()`
- All user-facing messages updated to reflect the new service
- Test cases verified and passing

### Migration
No migration required for existing deployments - just update the code and redeploy.

---

## v1.0.0 - 2025-06-21

### Added
- Initial release with fx.com replacement
- Telegram bot functionality
- URL detection and replacement
- Command handlers (/start, /help, /status)
- Error handling and logging
- Deployment configurations for Railway and Render
- Comprehensive testing suite
- Setup and demo scripts
