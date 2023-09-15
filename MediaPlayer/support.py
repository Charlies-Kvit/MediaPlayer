#  импортируем библиотеки
import telebot

from validate_email import validate_email
from interfaces.support_interface import Ui_Form
from PyQt5.QtWidgets import QWidget


#  Создаем окно и обработчики событий
class Support(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Поддержка')
        self.okButton.hide()
        self.messageLabel.hide()
        self.pushButton.clicked.connect(self.run)
        self.okButton.clicked.connect(self.exit)

    #  Проверяет существование почты, а затем(если она существует) отправляет текст через бота и выводит сообщение
    def run(self):
        mail = self.mail.text()
        problem = self.informationFromUser.toPlainText()
        try:
            if not bool(mail):
                mail = str(None)
            else:
                flag = validate_email(mail)
                if not flag:
                    self.label_2.setText("Такой почты нету!")
                    raise TypeError
            if not bool(problem):
                self.label_3.setText("Опишите проблему!!!")
                raise TypeError
            information = [mail, problem]
            token = '5786906777:AAF4Prtt-Xx8PNw6gXSDx7n6_6nu-SqF6LI'
            bot = telebot.TeleBot(token)
            chat_id = '2083681203'
            bot.send_message(chat_id, ":\n".join(information))
            self.pushButton.hide()
            self.informationFromUser.hide()
            self.mail.hide()
            self.label.hide()
            self.label_2.hide()
            self.label_3.hide()
            self.okButton.show()
            self.messageLabel.show()
        except Exception:
            pass

    #  Закрывает окно
    def exit(self):
        self.close()
