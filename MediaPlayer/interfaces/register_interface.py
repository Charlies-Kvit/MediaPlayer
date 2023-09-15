# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register_interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(507, 372)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.full_name = QtWidgets.QLineEdit(self.widget)
        self.full_name.setObjectName("full_name")
        self.horizontalLayout_2.addWidget(self.full_name)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.full_name_error = QtWidgets.QLabel(self.widget)
        self.full_name_error.setText("")
        self.full_name_error.setObjectName("full_name_error")
        self.verticalLayout_3.addWidget(self.full_name_error)
        self.verticalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.login = QtWidgets.QLineEdit(self.widget)
        self.login.setText("")
        self.login.setObjectName("login")
        self.horizontalLayout_3.addWidget(self.login)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.login_error = QtWidgets.QLabel(self.widget)
        self.login_error.setObjectName("login_error")
        self.verticalLayout_4.addWidget(self.login_error)
        self.verticalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.password = QtWidgets.QLineEdit(self.widget)
        self.password.setObjectName("password")
        self.horizontalLayout_4.addWidget(self.password)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.show_password = QtWidgets.QCheckBox(self.widget)
        self.show_password.setObjectName("show_password")
        self.verticalLayout.addWidget(self.show_password)
        self.password_error = QtWidgets.QLabel(self.widget)
        self.password_error.setObjectName("password_error")
        self.verticalLayout.addWidget(self.password_error)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.register_brn = QtWidgets.QPushButton(self.widget)
        self.register_brn.setObjectName("register_brn")
        self.verticalLayout_2.addWidget(self.register_brn)
        self.open_signin_btn = QtWidgets.QPushButton(self.widget)
        self.open_signin_btn.setObjectName("open_signin_btn")
        self.verticalLayout_2.addWidget(self.open_signin_btn)
        self.horizontalLayout.addWidget(self.widget)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.register_brn, self.password)
        Form.setTabOrder(self.password, self.show_password)
        Form.setTabOrder(self.show_password, self.full_name)
        Form.setTabOrder(self.full_name, self.login)
        Form.setTabOrder(self.login, self.open_signin_btn)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Регистрация"))
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Форма регистрации</span></p></body></html>"))
        self.label_4.setText(_translate("Form", "Полное имя:"))
        self.label_3.setText(_translate("Form", "Логин:         "))
        self.login_error.setText(_translate("Form", "TextLabel"))
        self.label_2.setText(_translate("Form", "Пароль:      "))
        self.show_password.setText(_translate("Form", "Показывать пароль"))
        self.password_error.setText(_translate("Form", "TextLabel"))
        self.register_brn.setText(_translate("Form", "Зарегистрироваться"))
        self.open_signin_btn.setText(_translate("Form", "Или вы уже зарегисрированы? Войти"))