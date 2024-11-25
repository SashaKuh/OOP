class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def save_to_database(self):
        print(f"Зберегти користувача {self.name} до базиданих.")

    def send_welcome_email(self):
        print(f"Надсилання вітального листа до {self.email}.")


