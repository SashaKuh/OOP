class MessageSender:
    def send(self, message, recipient):
        pass

class SmsSender(MessageSender):
    def send(self, message, recipient):
        print(f"Відправляю SMS '{message}' на номер {recipient}")

class EmailSender(MessageSender):
    def send(self, message, recipient):
        print(f"Відправляю Email '{message}' на адресу {recipient}")

def send_message(sender: MessageSender, message, recipient):
    sender.send(message, recipient)

sms_sender = SmsSender()
email_sender = EmailSender()

send_message(sms_sender, "Привіт!", "+380123456789")  
send_message(email_sender, "Привіт!", "test@example.com")
