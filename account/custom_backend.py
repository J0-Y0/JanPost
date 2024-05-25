from django.core.mail.backends.base import BaseEmailBackend
import requests


class CustomEmailBackend(BaseEmailBackend):
    def send_messages(self, email_messages):
        for message in email_messages:
            data = {
                "Subject": message.subject,
                "To": message.to[0],  # Assuming only one recipient
                "Content": message.body,
                "Username": "yosef.emyayu@bankofabyssinia.com",
                "Password": "1290@Boa",
            }
            url = "https://esb.bankofabyssinia.com:8443/sendEmail"
            headers = {"Content-Type": "application/json"}
            response = requests.post(url, json=data, headers=headers)
            # Check if the request was successful
            if response.status_code != 200:
                # Handle error
                pass
