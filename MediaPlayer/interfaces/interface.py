# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Interfaces_ui/interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(798, 496)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setObjectName("toolButton")
        self.verticalLayout.addWidget(self.toolButton)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.download_btn = QtWidgets.QPushButton(self.widget)
        self.download_btn.setObjectName("download_btn")
        self.verticalLayout_2.addWidget(self.download_btn)
        self.downloadCatalog_btn = QtWidgets.QPushButton(self.widget)
        self.downloadCatalog_btn.setObjectName("downloadCatalog_btn")
        self.verticalLayout_2.addWidget(self.downloadCatalog_btn)
        self.savePlaylist_btn = QtWidgets.QPushButton(self.widget)
        self.savePlaylist_btn.setObjectName("savePlaylist_btn")
        self.verticalLayout_2.addWidget(self.savePlaylist_btn)
        self.change_playlist_or_open_btn = QtWidgets.QPushButton(self.widget)
        self.change_playlist_or_open_btn.setObjectName("change_playlist_or_open_btn")
        self.verticalLayout_2.addWidget(self.change_playlist_or_open_btn)
        self.support_btn = QtWidgets.QPushButton(self.widget)
        self.support_btn.setObjectName("support_btn")
        self.verticalLayout_2.addWidget(self.support_btn)
        self.account_setting = QtWidgets.QPushButton(self.widget)
        self.account_setting.setObjectName("account_setting")
        self.verticalLayout_2.addWidget(self.account_setting)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.listWidget = QtWidgets.QListWidget(self.widget)
        self.listWidget.setObjectName("listWidget")
        self.horizontalLayout.addWidget(self.listWidget)
        self.verticalLayout.addWidget(self.widget)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.playBack_btn = QtWidgets.QPushButton(self.centralwidget)
        self.playBack_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Interfaces_ui\\../contents/play_back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.playBack_btn.setIcon(icon)
        self.playBack_btn.setObjectName("playBack_btn")
        self.horizontalLayout_2.addWidget(self.playBack_btn)
        self.stopButton = QtWidgets.QPushButton(self.centralwidget)
        self.stopButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Interfaces_ui\\../contents/stop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stopButton.setIcon(icon1)
        self.stopButton.setObjectName("stopButton")
        self.horizontalLayout_2.addWidget(self.stopButton)
        self.playPause_btn = QtWidgets.QPushButton(self.centralwidget)
        self.playPause_btn.setAutoFillBackground(True)
        self.playPause_btn.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Interfaces_ui\\../contents/pause_play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.playPause_btn.setIcon(icon2)
        self.playPause_btn.setObjectName("playPause_btn")
        self.horizontalLayout_2.addWidget(self.playPause_btn)
        self.playForward_btn = QtWidgets.QPushButton(self.centralwidget)
        self.playForward_btn.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Interfaces_ui\\../contents/play_forward.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.playForward_btn.setIcon(icon3)
        self.playForward_btn.setObjectName("playForward_btn")
        self.horizontalLayout_2.addWidget(self.playForward_btn)
        self.replay_btn = QtWidgets.QPushButton(self.centralwidget)
        self.replay_btn.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("Interfaces_ui\\../contents/restart.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.replay_btn.setIcon(icon4)
        self.replay_btn.setObjectName("replay_btn")
        self.horizontalLayout_2.addWidget(self.replay_btn)
        self.random_btn = QtWidgets.QPushButton(self.centralwidget)
        self.random_btn.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("Interfaces_ui\\../contents/random.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.random_btn.setIcon(icon5)
        self.random_btn.setObjectName("random_btn")
        self.horizontalLayout_2.addWidget(self.random_btn)
        self.timePlaying = QtWidgets.QLabel(self.centralwidget)
        self.timePlaying.setObjectName("timePlaying")
        self.horizontalLayout_2.addWidget(self.timePlaying)
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalLayout_2.addWidget(self.horizontalSlider)
        self.lenTimeMusic = QtWidgets.QLabel(self.centralwidget)
        self.lenTimeMusic.setObjectName("lenTimeMusic")
        self.horizontalLayout_2.addWidget(self.lenTimeMusic)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 798, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Music Popgdse"))
        self.toolButton.setText(_translate("MainWindow", "Аноним"))
        self.download_btn.setText(_translate("MainWindow", "Открыть файл"))
        self.downloadCatalog_btn.setText(_translate("MainWindow", "Окрыть папку"))
        self.savePlaylist_btn.setText(_translate("MainWindow", "Сохранить плейлист"))
        self.change_playlist_or_open_btn.setText(_translate("MainWindow", "Изменить плейлист или открыть его"))
        self.support_btn.setText(_translate("MainWindow", "Поддержка"))
        self.account_setting.setText(_translate("MainWindow", "Изменить или создать аккаунт"))
        self.timePlaying.setText(_translate("MainWindow", "00:00"))
        self.lenTimeMusic.setText(_translate("MainWindow", "00:00"))