import time
import requests

msg = input("Insert Spam Message - ")
webhook = input("Webhook Url - ")

def spam(msg, webhook):
    while True:
        data = requests.post(webhook, json={'content': msg})
        print(data.text)
        print(data.status_code)
        if data.status_code == 204:
            print(f"Sent Message {msg}")
        else:
            try:
                time.sleep(data.json()["retry_after"]/1000)
            except:
                pass
            gian_top = 1
            while gian_top == 1:
                spam(msg, webhook)
                
spam(msg, webhook)
