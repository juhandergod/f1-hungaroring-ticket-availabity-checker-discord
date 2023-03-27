import requests
import json
import os

# Replace the webhook URL with your own webhook URL
WEBHOOK_URL = os.getenv("WEBHOOK_URL")


def send_message(message_text):
    # Create the message payload
    message = {
        "content": message_text
    }

    # Send the HTTP request
    response = requests.post(WEBHOOK_URL, data=json.dumps(message), headers={"Content-Type": "application/json"})

    # Check the response status code to make sure the message was sent successfully
    if response.status_code == 204:
        print("Notification sent successfully!")
    else:
        print("Failed to send notification.")
