# import subprocess

# def read_pm2_logs(app_name):
#   print("[Server Monitor]: Running")
#   try:
#     cmd = f"pm2 logs {app_name} --json"
#     result = subprocess.run(cmd, shell=True, capture_output=True, text=True)

#     # Read and print logs line by line in real-time
#     for line in result.stdout:
#         print(line.strip())

#   except Exception as e:
#     print(f"Error reading PM2 Logs: {e}")

# read_pm2_logs('index')

import subprocess
import requests
from dotenv import load_dotenv
import os

load_dotenv()

def listen_to_pm2_logs(app_name):
    print("Starting Server")
    try:
        # Run PM2 logs command and capture the output
        cmd = f"pm2 logs {app_name} --json"
        process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, text=True)

        # Read and print logs line by line in real-time
        for line in process.stdout:
            print("New Log")
            if "ERROR" in line.strip().upper():
                # url = 
                t = requests.post(os.environ.get("WEB_HOOK_URL"), json = { 
                    "username": os.environ.get("BOT_NAME"),
                    "avatar_url": os.environ.get("BOT_AVATAR"), 
                    "content": "Server Monitor Alert",
                    "embeds": [
                        {    
                            "author": {
                                "name": os.environ.get("PROJECT_NAME"),
                            },
                            "title": "An Error has Occurred in the Server",
                            "description": f'```\n{line.strip()}\n```',
                            "color": int("ff0000", 16),
                            "footer": {
                                "text": "Please review the server ASAP"
                            }
                        },
                        
                    ]
                })
                print(t.text)

        # Wait for the process to finish (Ctrl+C to exit)
        process.wait()

    except Exception as e:
        print(f"Error listening to PM2 logs: {e}")

# Replace 'your_app_name' with the actual name of your PM2 app
listen_to_pm2_logs('index')

