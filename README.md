# Server Monitor

This is a simple **PM2** monitor built using **Python**. It sends alert using Discord Webhook for any error that occurs in the system.

## Installation

```bash
  # After you have cloned the project
  # Create a virtual env
  python3 -m venv .venv
  # activatet the env
  . .venv/bin/activate
  # Install requirements
  pip3 install -r requirements.txt
  # Create .env
  cat env-example > .env
  # Start the service using pm2
  pm2 start core/main.py --interpreter /home/user/server-monitor/.venv/bin/python3 --name server-monitor
  # make sure that the path to your interpreter is correct
```

### Learn More About Discord Webhook Payload

https://birdie0.github.io/discord-webhooks-guide/discord_webhook.html
