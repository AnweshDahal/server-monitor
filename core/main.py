import subprocess
import requests
from dotenv import load_dotenv
import os
import re

load_dotenv()


def listen_to_pm2_logs(app_name):
    print("Starting Server")
    try:
        # Run PM2 logs command and capture the output
        cmd = f"pm2 logs {app_name} --json"
        process = subprocess.Popen(
            cmd, shell=True, stdout=subprocess.PIPE, text=True)

        print(process)
        # Read and print logs line by line in real-time
        for line in process.stdout:
            if "ERROR" in line.strip().upper():
                brevo_error = re.findall("MESSAGE_SIZE_EXCEEDED", line.strip())

                message = line.strip() if len(brevo_error) <= 0 else "Message Size Error"

                t = requests.post(os.environ.get("WEB_HOOK_URL"), json={
                    "cards": [
                        {
                            "header": {
                                "title": os.environ.get("BOT_NAME"),
                                "subtitle": os.environ.get("PROJECT_NAME")
                            },
                            "sections": [
                                {
                                    "header": "An Error has Occurred in the Server",
                                    "widgets": [
                                        {
                                            "textParagraph": {
                                                "text": message
                                            }
                                        }
                                    ]
                                }
                            ]
                        }
                    ]

                })

                if t.status_code == 200:
                    print("Error Reported Successfully")
                else:
                    print(
                        f'Failed to send Report. Status code: {t.status_code}')

        # Wait for the process to finish (Ctrl+C to exit)
        process.wait()

    except Exception as e:
        print(f"Error listening to PM2 logs: {e}")


# Replace 'your_app_name' with the actual name of your PM2 app
listen_to_pm2_logs(os.environ.get("APP_NAME"))
