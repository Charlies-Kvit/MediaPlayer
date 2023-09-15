#  Импортируем нужные библиотеки и файлы
import sys
import os
import sqlite3
import bcrypt
import shutil

from PasswordCheckClass import (CheckPassword, LengthError, LetterError, DigitError)
from interfaces.save_playlist_interface import Ui_Form as SavePlaylist_Form
from mutagen.mp3 import MP3
from interfaces.register_interface import Ui_Form as Register_Form
from interfaces.signin_interface import Ui_Form as SignIn_Form
from interfaces.change_playlist_interface import Ui_Form as Change_Form
from interfaces.interface import Ui_MainWindow
from support import Support
from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication, QFileDialog, QLineEdit, QMessageBox, QShortcut
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QMediaPlaylist
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QIcon, QKeySequence


#  Создаем основной класс
class MediaPlayer(QMainWindow, Ui_MainWindow):
    #  Все инициализируем и обрабатываем все возможные нажатия кнопок
    def __init__(self, register_flag):
        super().__init__()
        self.setupUi(self)
        self.data, self.index, self.play_mod = [], 0, 2
        self.player = QMediaPlayer(self)
        self.playlist = QMediaPlaylist(self)
        self.player.setPlaylist(self.playlist)
        self.player_music, self.load_music = False, False
        '''self.play_pause_shortcut = QShortcut(QKeySequence('MediaPlayPause'), self)
        self.forward_shortcut = QShortcut(QKeySequence('MediaTrackNext'), self)
        self.back_shortcut = QShortcut(QKeySequence('MediaTrackPrevious'), self)
        self.play_pause_shortcut.activated.connect(self.player_music)
        self.forward_shortcut.activated.connect(self.run_forward)
        self.back_shortcut.activated.connect(self.run_back)'''
        self.horizontalSlider.sliderReleased.connect(self.change_time)
        self.player.positionChanged.connect(self.print_time_music)
        self.playlist.currentIndexChanged.connect(self.len_music)
        self.download_btn.clicked.connect(self.download_file)
        self.listWidget.itemClicked.connect(self.play_music)
        self.playPause_btn.clicked.connect(self.run_pause)
        self.playBack_btn.clicked.connect(self.run_back)
        self.playForward_btn.clicked.connect(self.run_forward)
        self.stopButton.clicked.connect(self.stop_music)
        self.downloadCatalog_btn.clicked.connect(self.download_playlist)
        self.support_btn.clicked.connect(self.support)
        self.savePlaylist_btn.clicked.connect(self.save_playlist)
        self.replay_btn.clicked.connect(self.replay)
        self.random_btn.clicked.connect(self.random)
        self.account_setting.clicked.connect(self.sign_in_window)
        self.listWidget.doubleClicked.connect(self.delete)
        self.change_playlist_or_open_btn.clicked.connect(self.change_playlist)
        self.show()
        if register_flag:
            self.register_form_window(True)
        else:
            with open('config/account_info.txt', 'rt') as f:
                data = f.readlines()
                name = data[0][:-1]
                self.login = data[1][:-1]
            self.toolButton.setText(name)

    #  Показывает окно входа
    def sign_in_window(self):
        self.sign_in_w = SignInForm()
        self.sign_in_w.show()

    #  Отвечает за действие передвижения ... слайдера???
    def change_time(self):
        if bool(self.data):
            self.player.setPosition(self.horizontalSlider.sliderPosition() * 1000)
        else:
            self.horizontalSlider.setSliderPosition(0)

    #  Показывает окно регистрации
    def register_form_window(self, flag=False):
        self.window_register_form = RegisterForm(flag)
        self.window_register_form.show()

    #  Загружает музыку из папки в плеер
    def download_playlist(self, input_catalog=''):
        try:
            if not input_catalog:
                catalog = QFileDialog.getExistingDirectory(self, str("Open Directory"),
                                                           "/home",
                                                           QFileDialog.ShowDirsOnly
                                                           | QFileDialog.DontResolveSymlinks)
            else:
                catalog = input_catalog
            for file in os.listdir(catalog):
                try:
                    if file[file.rfind('.') + 1:] != 'mp3':
                        continue
                    elif os.path.join(catalog, file) in self.data:
                        continue
                    self.data.append(os.path.join(catalog, file))
                    self.listWidget.addItem(file[:file.rfind('.')])
                    url = QUrl.fromLocalFile(os.path.join(catalog, file))
                    self.playlist.addMedia(QMediaContent(url))
                except Exception:
                    continue
            self.run_pause()
        except Exception:
            pass

    #  Отвечает за то, что бы показать сколько времени прошло с начала проигрывания mp3 файла
    def print_time_music(self):
        time = int(self.player.position() / 1000)
        #  a = self.horizontalSlider.value() + 1 (старый код)
        self.horizontalSlider.setSliderPosition(time)
        minutes = int((time - time % 60) / 60)
        seconds = int(time % 60)
        if seconds < 10 and minutes < 10:
            self.timePlaying.setText(f'0{minutes}:0{seconds}')
        elif seconds >= 10 and minutes < 10:
            self.timePlaying.setText(f'0{minutes}:{seconds}')
        elif seconds >= 10 and minutes >= 10:
            self.timePlaying.setText(f'{minutes}:{seconds}')
        else:
            self.timePlaying.setText(f'{minutes}:0{seconds}')

    #  загружает mp3 файл в плеер
    def download_file(self):
        try:
            fname = QFileDialog.getOpenFileName(self, 'Download Music',
                                               '/home', '(*.mp3)')[0]
            if fname in self.data:
                raise TypeError
            self.data.append(fname)
            music = fname[fname.rfind('/') + 1:fname.rfind('.')]
            self.listWidget.addItem(music)
            url = QUrl.fromLocalFile(fname)
            self.playlist.addMedia(QMediaContent(url))
        except Exception:
            pass

    #  Удаляет выбранную песню из проигрывания
    def delete(self):
        music = self.listWidget.currentRow()
        a = self.data.count(music)
        self.listWidget.takeItem(music)
        del self.data[a]

    #  Выделяет проигрываемый файл и начинает его воспроизведение
    def play_music(self):
        try:
            music = self.listWidget.currentRow()
            self.index = music
            self.playlist.setCurrentIndex(music)
            self.player.play()
            self.load_music = True
            self.player_music = True
            self.len_music()
        except Exception:
            pass

    #  Останавливает музыку полностью
    def stop_music(self):
        self.player_music = False
        self.player.stop()
        self.horizontalSlider.setSliderPosition(0)
        self.index = self.playlist.currentIndex()

    #  Вычисляет и выводит длину воспроизведения музыки в виде: 3:10
    def len_music(self):
        music = MP3(self.data[self.playlist.currentIndex()])
        self.listWidget.setCurrentRow(self.playlist.currentIndex())
        self.index += self.playlist.currentIndex()
        minutes = int((music.info.length - music.info.length % 60) / 60)
        seconds = int(music.info.length % 60)
        self.horizontalSlider.setMaximum(int(music.info.length))
        self.horizontalSlider.setSliderPosition(0)
        if seconds < 10 and minutes < 10:
            len_m = f'0{minutes}:0{seconds}'
        elif seconds > 10 and minutes < 10:
            len_m = f'0{minutes}:{seconds}'
        elif seconds < 10 and minutes > 10:
            len_m = f'{minutes}:0{seconds}'
        else:
            len_m = f'{minutes}:{seconds}'
        self.lenTimeMusic.setText(len_m)

    #  Ставит на паузу, либо продолжает воспроизведение
    def run_pause(self):
        if bool(self.data):
            if self.player_music:
                self.player.pause()
                self.player_music = False
            else:
                if not self.load_music:
                    try:
                        self.playlist.setCurrentIndex(self.index)
                        self.load_music = True
                        self.player.play()
                        self.player_music = True
                        self.len_music()
                    except Exception:
                        pass
                else:
                    self.player.play()
                    self.player_music = True
            self.listWidget.setCurrentRow(self.index)

    #  Перемотка на прошлую песню
    def run_back(self):
        if bool(self.data):
            index = self.playlist.currentIndex()
            if index - 1 < 0:
                index = len(self.data) - 1
            else:
                index -= 1
            self.index = index
            self.playlist.setCurrentIndex(index)
            self.player.play()
            self.listWidget.setCurrentRow(index)
            self.len_music()

    #  Перемотка на следующую песню
    def run_forward(self):
        if bool(self.data):
            index = self.playlist.currentIndex()
            if index + 1 > len(self.data) - 1:
                index = 0
            else:
                index += 1
            self.index = index
            self.playlist.setCurrentIndex(index)
            self.player.play()
            self.listWidget.setCurrentRow(index)
            self.len_music()

    #  Сохраняет плейлист локально в папку для дальнейшей работы
    def save_playlist(self):
        if bool(self.data):
            self.save_playlist_window = SavePlaylist()
            self.save_playlist_window.show()

    #  Отвечает за замену типа проигрывания: повторять одну композицию, весь плейлист, от начала до конца и остановиться
    def replay(self):
        if bool(self.data):
            try:
                if self.play_mod == 2:
                    self.playlist.setPlaybackMode(1)
                    self.play_mod = 1
                    self.replay_btn.setIcon(QIcon('contents/restart2.png'))
                    self.random_btn.setIcon(QIcon('contents/random.png'))
                elif self.play_mod == 1:
                    self.play_mod = 3
                    self.playlist.setPlaybackMode(3)
                    self.replay_btn.setIcon(QIcon('contents/restart3.png'))
                    self.random_btn.setIcon(QIcon('contents/random.png'))
                else:
                    self.play_mod = 2
                    self.playlist.setPlaybackMode(2)
                    self.replay_btn.setIcon(QIcon('contents/restart.png'))
                    self.random_btn.setIcon(QIcon('contents/random.png'))
            except Exception:
                pass

    #  Отвечает за типы проигрывания: рандом и по умолчанию(от начала до конца по порядку)
    def random(self):
        if bool(self.data):
            if self.play_mod != 4:
                self.playlist.setPlaybackMode(4)
                self.play_mod = 4
                self.random_btn.setIcon(QIcon('contents/random2.png'))
                self.replay_btn.setIcon(QIcon('contents/restart.png'))
            else:
                self.play_mod = 2
                self.playlist.setPlaybackMode(2)
                self.replay_btn.setIcon(QIcon('contents/restart.png'))
                self.random_btn.setIcon(QIcon('contents/random.png'))

    #  Открывает окно редактирования содержимого плейлиста
    def change_playlist(self):
        self.change_window = ChangePlaylist()
        self.change_window.show()

    #  Открывает окно поддержки
    def support(self):
        self.support = Support()
        self.support.show()


#  Регистрационное окно
class RegisterForm(QWidget, Register_Form):
    def __init__(self, first_register=False):
        super().__init__()
        self.first_register = first_register
        self.all_right = True
        self.banned_symbols = [
            '"', "'", ',', '.', '/', '\\', '+', '=', '#',
            ':', ';', '%', '^', '|'
        ]
        self.setupUi(self)
        if first_register:
            self.open_signin_btn.setEnabled(False)
        self.data_base = sqlite3.connect('config/app_db.sqlite')
        self.cur = self.data_base.cursor()
        users_logins = self.cur.execute("""
            SELECT login FROM Users
        """).fetchall()
        self.users_logins = [el[0] for el in users_logins]
        self.password.setEchoMode(QLineEdit.Password)
        self.full_name_error.hide()
        self.login_error.hide()
        self.password_error.hide()
        self.show_password_user = False
        self.password.textChanged.connect(self.check_password)
        self.full_name.textChanged.connect(self.check_fullname)
        self.login.textChanged.connect(self.check_login)
        self.show_password.clicked.connect(self.show_hide_password)
        self.register_brn.clicked.connect(self.register)
        self.open_signin_btn.clicked.connect(self.sign_in_window)

    #  Если пользователь нажимает на "Показать пароль", то он будет виден
    def show_hide_password(self):
        if self.show_password_user:
            self.show_password_user = False
            self.password.setEchoMode(QLineEdit.Password)
        else:
            self.show_password_user = True
            self.password.setEchoMode(QLineEdit.Normal)

    #  Проверяет соответствие имени, введенного пользователем, на наличие запрещенных символов в реальном времени
    def check_fullname(self):
        self.full_name_error.hide()
        for el in self.full_name.text():
            if el in self.banned_symbols:
                self.full_name_error.setText(
                    "В имени могут присутствовать только"
                    " буквы и некоторые символы"
                )
                self.full_name_error.show()
                self.all_right = False
                break
        else:
            self.all_right = True

    #  То же самое, что и с check_fullname, только проверяется еще и то, не находится ли уже логин в базе данных
    def check_login(self):
        self.login_error.hide()
        for el in self.login.text():
            if el in self.banned_symbols:
                if el == "'":
                    self.login_error.setText(
                        f"В логине не может присутствовать {el}"
                    )
                    self.login_error.show()
                    self.all_right = False
                    break
                else:
                    self.login_error.setText(
                        f'В логине не может присутствовать {el}'
                    )
                    self.login_error.show()
                    self.all_right = False
                    break
        else:
            if self.login.text() in self.users_logins:
                self.login_error.setText(
                    'Этот логин уже занят. Попробуйте другой.'
                )
                self.login_error.show()
                self.all_right = False
            else:
                self.all_right = True

    #  Проверяет соответствие пароля некоторым критериям
    def check_password(self):
        try:
            self.password_error.hide()
            CheckPassword(self.password.text())
        except LengthError:
            self.password_error.setText(
                'Длина пароля должна быть больше 8 символов!!!'
            )
            self.password_error.show()
            self.all_right = False
        except LetterError:
            self.password_error.setText(
                'В пароле должны быть символы обеих регистров!!!'
            )
            self.password_error.show()
            self.all_right = False
        except DigitError:
            self.password_error.setText(
                'В пароле должны присутствовать цифры!!!'
            )
            self.password_error.show()
            self.all_right = False
        except Exception:
            pass
        else:
            self.all_right = True

    #  Если пользователь пытается закрть окно при первом запуске, то ничего не выйдет)
    def closeEvent(self, event):
        if self.first_register:
            message = QMessageBox(
                QMessageBox.Information, 'Регистрация обязательна', 'Зарегестрируйтесь!'
            )
            message.exec()
            event.ignore()
        else:
            self.close()
            self.data_base.close()

    #  Заносит нового пользователя в базу данных
    def register(self):
        try:
            if self.full_name.text() == '':
                raise TypeError()
            elif self.login.text() == '':
                raise TypeError()
            elif self.password.text() == '':
                raise TypeError()
            elif not self.all_right:
                raise TypeError()
            else:
                username = self.full_name.text()
                login = self.login.text()
                password = self.password.text()
                salt_and_key = str(bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()))[2:-1]
                self.cur.execute(f"""
                INSERT INTO Hash_passwords(password) VALUES("{salt_and_key}")
                """)
                self.data_base.commit()
                user_id = int(self.cur.execute(f"""
                SELECT id FROM Hash_passwords
                WHERE password = "{salt_and_key}"
                """).fetchall()[0][0])
                self.cur.execute(f"""
                INSERT INTO Users(name, login, passwordID) VALUES('{username}', '{login}', '{user_id}')
                """)
                with open('config/account_info.txt', 'w') as fw:
                    print(username, file=fw)
                    print(login, file=fw)
                App.login = login
                App.toolButton.setText(username)
                if self.first_register:
                    self.first_register = False
                os.mkdir(os.path.join('users', login))
                with open(os.path.join('users', login, 'playlists.txt'), 'w') as fw:
                    fw.close()
                self.data_base.commit()
                self.data_base.close()
                self.close()
        except Exception as error:
            print(error)
            text = 'Все поля обязательны для заполнения!!!'
            message = QMessageBox(
                QMessageBox.Critical, text, text
            )
            message.exec()

    #  Открывает окно (Войти)
    def sign_in_window(self):
        self.sign_window = SignInForm()
        self.data_base.close()
        self.sign_window.show()
        self.close()


#  Форма входа
class SignInForm(QWidget, SignIn_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.password.setEchoMode(QLineEdit.Password)
        self.show_password_user = False
        self.error_label.hide()
        self.data_base = sqlite3.connect('config/app_db.sqlite')
        self.cur = self.data_base.cursor()
        self.open_register_btn.clicked.connect(self.open_register_window)
        self.signin_btn.clicked.connect(self.signin)
        self.checkBox.clicked.connect(self.show_hide_password)

    #  Проверяет логин и пароль с данными в базе данных
    def signin(self):
        try:
            input_login = self.login.text()
            input_password = self.password.text()
            password = self.cur.execute(f"""
            SELECT password FROM Hash_passwords
            WHERE id=(
            SELECT userID FROM Users
            WHERE login = '{input_login}'
            )""").fetchall()[0][0]
            if not bool(password):
                raise TypeError("Неверный логин!!!")
            flag_value = bcrypt.checkpw(input_password.encode('utf-8'), password.encode('utf-8'))
            if not flag_value:
                raise TypeError("Неверный пароль!!!")
            with open('config/account_info.txt', 'w') as fw:
                username = self.cur.execute(f"""
                SELECT name FROM Users
                WHERE login = '{input_login}'
                """).fetchall()[0][0]
                print(username, file=fw)
                print(input_login, file=fw)
            App.toolButton.setText(username)
            App.login = input_login
            self.close()
        except Exception as error:
            msgBox = QMessageBox()
            msgBox.setText(str(error))
            msgBox.exec()

    #  Либо показывает пароль, либо нет
    def show_hide_password(self):
        if self.show_password_user:
            self.show_password_user = False
            self.password.setEchoMode(QLineEdit.Password)
        else:
            self.show_password_user = True
            self.password.setEchoMode(QLineEdit.Normal)

    #  При закрытии окна закрывается соединение с базой данных
    def closeEvent(self, event):
        self.data_base.close()

    #  Открывает окно регистрации
    def open_register_window(self):
        self.register_window = RegisterForm()
        self.data_base.close()
        self.register_window.show()
        self.close()


# Сохраняет план проигрывания копируя файлы в отдельную директорию под названием, которое ввел пользователь
class SavePlaylist(QWidget, SavePlaylist_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.data_base = sqlite3.connect('config/app_db.sqlite')
        self.cur = self.data_base.cursor()
        self.save_btn.clicked.connect(self.save_playlist)

    def save_playlist(self):
        try:
            name = self.playlist_name.text()
            with open(os.path.join('users', App.login, 'playlists.txt'), 'rt') as f:
                playlists = f.readlines()
            for el in playlists:
                if name in el:
                    print(name, el)
                    raise TypeError
            with open(os.path.join('users', App.login, 'playlists.txt'), 'a+') as fw:
                print(name, file=fw)
            user_id = self.cur.execute(f"""
            SELECT userID FROM Users
            WHERE login = '{App.login}'
            """).fetchall()[0][0]
            self.cur.execute(f"""
            INSERT INTO Playlists(name_playlist, user) VALUES('{name}', '{user_id}')
            """)
            os.mkdir(os.path.join('users', App.login, name))
            way = os.path.join('users', App.login, name)
            for music in App.data:
                shutil.copy(music, way)
            self.close()
            self.data_base.commit()
            self.data_base.close()
        except Exception as error:
            print(error)
            msg = QMessageBox()
            msg.setText("Этот плейлист уже существует!!!!")
            msg.exec()


#  Дает возможность удалять плейлисты и менять их содержимое, а также открыть этот плейлист для прослушивания
class ChangePlaylist(QWidget, Change_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.fill_combobox()
        self.set_playlist()
        self.data_base = sqlite3.connect('config/app_db.sqlite')
        self.cur = self.data_base.cursor()
        self.add_song_in_playlist.clicked.connect(self.add_song)
        self.delete_song_btn.clicked.connect(self.delete_song)
        self.playlists.currentIndexChanged.connect(self.set_playlist)
        self.delete_playlist_btn.clicked.connect(self.delete_playlist)
        self.listWidget.doubleClicked.connect(self.delete_song)
        self.open_playlist.clicked.connect(self.open_playlist_in_player)

    #  Открывает выбранный плейлист для прослушивания
    def open_playlist_in_player(self):
        way = os.path.join('users', App.login, self.playlist)
        App.data.clear()
        App.listWidget.clear()
        App.playlist.clear()
        App.download_playlist(way)
        self.close()

    #  Закрывает соединения с базой данных
    def closeEvent(self, event):
        self.data_base.close()

    #  Удаляет песню из папки, то есть из плейлиста
    def delete_song(self):
        song = self.listWidget.currentItem().text()
        self.listWidget.takeItem(self.listWidget.currentRow())
        way = os.path.join(os.path.dirname(__file__), 'users', App.login, self.playlist)
        for file in os.listdir(way):
            if file[file.rfind('/') + 1:file.rfind('.')] == song:
                way = os.path.join('users', App.login, self.playlist, file)
                break
        os.remove(way)

    #  Добавляет песню в плейлист
    def add_song(self):
        try:
            fname = QFileDialog.getOpenFileName(self, 'Download Music',
                                               '/home', '(*.mp3)')[0]
            music = fname[fname.rfind('/') + 1:fname.rfind('.')]
            self.listWidget.addItem(music)
            way = os.path.join('users', App.login, self.playlist)
            shutil.copy(fname, way)
        except Exception:
            pass

    #  Удаляет выбранный плейлист
    def delete_playlist(self):
        valid = QMessageBox.question(
            self, '', f'Точно удалить {self.playlist}?',
            QMessageBox.Yes, QMessageBox.No)
        if valid == QMessageBox.Yes:
            way = os.path.join('users', App.login, self.playlist)
            self.cur.execute(f"""
            DELETE FROM playlists
            WHERE name_playlist = '{self.playlist}' AND user = (
                SELECT user FROM Users
                    WHERE login = '{App.login}'
            ) 
            """)
            for file in os.listdir(way):
                os.remove(os.path.join(way, file))
            os.rmdir(os.path.join('users', App.login, self.playlist))
            print(self.playlists_list)
            del self.playlists_list[self.playlists_list.index(self.playlist)]
            with open(os.path.join('users', App.login, 'playlists.txt'), 'w') as fw:
                for el in self.playlists_list:
                    print(el)
                    print(el, file=fw)
            self.fill_combobox()
            # self.set_playlist()
            self.data_base.commit()

    #  Узнает имя выбранного плейлиста на данный момент
    def set_playlist(self):
        self.playlists.setCurrentIndex(0)
        self.playlist = self.playlists.currentText()
        print(self.playlist)
        way = os.path.join('users', App.login, self.playlist)
        self.listWidget.clear()
        for file in os.listdir(way):
            try:
                if file[file.rfind(".") + 1:] != 'mp3':
                    continue
                self.listWidget.addItem(file[:file.rfind('.')])
            except Exception:
                pass

    #  Заполняет комбобокс именами плейлистов
    def fill_combobox(self):
        self.playlists.clear()
        with open(os.path.join('users', App.login, 'playlists.txt'), 'rt') as f:
            data = f.readlines()
            data = [i.strip() for i in data]
        self.playlists_list = data
        for playlist in data:
            self.playlists.addItem(playlist)


#  Запуск программы
if __name__ == "__main__":
    try:
        flag = False
        if not os.path.exists('users'):
            flag = True
            os.mkdir('users')
        app = QApplication(sys.argv)
        App = MediaPlayer(flag)
        App.show()
        sys.exit(app.exec_())
    except Exception as error:
        print(error)

