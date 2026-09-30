# Discord Custom Activity

A small Python experiment that displays a custom Rich Presence activity in the Discord desktop app.

## Requirements

- Python 3.10 or newer
- The Discord desktop app, running and signed in on the same computer
- An application created in the [Discord Developer Portal](https://discord.com/developers/applications)

## Run locally

```sh
git clone https://github.com/c-jien/discord-custom-activity.git
cd discord-custom-activity
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
cp .env.example .env
```

Set `DISCORD_CLIENT_ID` in `.env` to the application's **Application ID**. Do not use a bot token, client secret, or Discord password. Then, in a macOS/Linux shell:

```sh
set -a
. ./.env
set +a
python discord-customapp.py
```

On Windows, activate `.venv\Scripts\Activate.ps1` in PowerShell and set `$env:DISCORD_CLIENT_ID = "your-application-id"` before running the script.

Edit `details` and `state` in the script to customize the activity. The elapsed-time display starts when the script launches. Press Ctrl+C to stop.

This is a personal learning project. It uses a local Discord connection and does not require a hosted service.
