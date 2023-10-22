#imports
import requests
import time

loop = "Y"
print("You need 5 webhook links for this!")
webhook = input("Enter webhook link: ")
webhook1 = input("Enter webhook link: ")
webhook2 = input("Enter webhook link: ")
webhook3 = input("Enter webhook link: ")
webhook4 = input("Enter webhook link: ")
text = input("Enter text to spam: ")

payload = {
    "content": f"{text}"
    }

loop = input("Start spamming? (Y/N): ").capitalize()

while loop =="Y":
    print("Sending", text, "to webhook.")
    response = requests.post(webhook, json=payload)
    response1 = requests.post(webhook1, json=payload)
    response2 = requests.post(webhook2, json=payload)
    response3 = requests.post(webhook3, json=payload)
    response4 = requests.post(webhook4, json=payload)
    print("Message sent successfully!")

else:
    print("Message failed to send!")
    time.sleep(3)
    exit()
