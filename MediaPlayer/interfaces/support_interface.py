# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'support_interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(490, 399)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.messageLabel = QtWidgets.QLabel(self.widget)
        self.messageLabel.setObjectName("messageLabel")
        self.verticalLayout_2.addWidget(self.messageLabel)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.mail = QtWidgets.QLineEdit(self.widget)
        self.mail.setObjectName("mail")
        self.horizontalLayout_2.addWidget(self.mail)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.informationFromUser = QtWidgets.QTextEdit(self.widget)
        self.informationFromUser.setObjectName("informationFromUser")
        self.verticalLayout.addWidget(self.informationFromUser)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.okButton = QtWidgets.QPushButton(self.widget)
        self.okButton.setObjectName("okButton")
        self.verticalLayout_2.addWidget(self.okButton)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        self.horizontalLayout.addWidget(self.widget)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "<html><head/><body><p>Версия: 0.001(alpha)</p><p>Разработчик: Бутович Глеб Николаевич</p><p>Если вдруг возникли проблемы, заполните форму.</p></body></html>"))
        self.messageLabel.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Все отправлено! </span></p><p>Я постараюсь исправить этот баг в скором времени!</p></body></html>"))
        self.label_2.setText(_translate("Form", "Почта(необязательно)"))
        self.label_3.setText(_translate("Form", "Опишите проблему"))
        self.okButton.setText(_translate("Form", "Ok"))
        self.pushButton.setText(_translate("Form", "Отправить"))
