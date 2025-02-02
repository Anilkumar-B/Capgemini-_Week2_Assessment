"""•	14. Implement method overriding for a `Notification` class where `send()` 
is overridden in `EmailNotification` and `SMSNotification`."""

class Notification:
    def __init__(self, message):
        self.message = message
    def send(self):
        print("Sending notification...")
class EmailNotification(Notification):
    def send(self):
        print("Sending email notification...")
class SMSNotification(Notification):
    def send(self):
        print("Sending SMS notification...")
notification=EmailNotification("Hello we are send email regarding to the query")
notification.send()
notification=SMSNotification("Hello we are sending SMS regarding to the query")
notification.send()

