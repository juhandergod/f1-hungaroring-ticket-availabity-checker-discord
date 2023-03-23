import requests
import json

# Replace the webhook URL with your own webhook URL
WEBHOOK_URL = "https://discord.com/api/webhooks/1088398861854310480/xzi0_PpEjMFMG7M9XtuW2G5iXCxn_sPr7eqQSRTTRsk5-E1ry0vp38-PtAD4UJgnhG-f"

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
