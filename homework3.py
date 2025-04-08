class Notification:
    def send(self):
        pass

    def __init__(self, massage):
        self._massage = massage
    def set_massage(self, massage):
        self._massage = massage
    def get_massage(self):
        return self._massage


class SMSNotification(Notification):
    def send(self):
        return f"SMS Сообщение: {self._massage}"
    
class EmailNotification(Notification):
    def send(self):
        return f"Почтовое сообщение: {self._massage}"
    
sms_notification1 = SMSNotification("СМС сообщение1")
sms_notification2 = SMSNotification("СМС сообщение2")
email_notification1 = EmailNotification("Почта 1")
email_notification2 = EmailNotification("Почта 2")
notifications = [sms_notification1, sms_notification2, email_notification1, email_notification2]
