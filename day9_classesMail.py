import datetime

class Message4user():
    user_details = []
    messages = []
    base_message = """Hi, {name}!
    Thank you for your purcase on {date}.
    You total was ${total}.
    We hope you like it and we'll be glad to see you again.

    Have a great day,
    team BuyCheapShit LTD
    """

    def add_user(self, name, anount, email=None):
        name = name[0].upper() + name[1:].lower()
        amount = "%.2f" %(amount)
        detail = {
        "name" = name,
        "amount" = amount,
        }
        today = datetime.date.today()
        date_text = '{bla.month}/{bla.day}/{bla.year}'.format(bla=today)
        datail['date'] = date_text
        if email is not None:
            detail["email"] = email
        self.user_details.append(detail)
    def get_details(self):
        return self.user_details
    def make_messages(self):
        if len(self.user_details) > 0:
            for detail in self.get_details():
                name = detail["name"]
                amount = detail["amount"]
                date = detail["date"]
                message = self.base_message
                new_msg = message.format(
                    name = name,
                    date = date,
                    total = amount
                )
                self.messages.append(new_msg)
            return self.messages
        return []

obj = Message4user()
obj.add_user("Justin", 123.2335, email='hi@your.domain')
obj.add_user("Sara", 96.96)
obj.make_messages()
                
