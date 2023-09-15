#  Импортируем библиотеки
import string

#  Создаем нужные списки и словари
RUS_LOWER = 'йцукенгшщзхъфывапролджэячсмитьбюё'
RUS_UP = 'ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮЁ'
combinations = ['qwe', 'wer', 'ert', 'rty', 'tyu', 'yui', 'uio', 'iop',
                'asd', 'sdf', 'dfg', 'fgh', 'ghj', 'hjk', 'jkl', 'zxc',
                'xcv', 'cvb', 'vbn', 'bnm', 'йцу', 'цук', 'уке', 'кен', 
                'енг', 'нгш', 'гшщ', 'шщз', 'щзх', 'зхъ', 'фыв', 'ыва',
                'вап', 'апр', 'про', 'рол', 'олд', 'лдж', 'джэ', 'ячс', 
                'чсм', 'сми', 'мит', 'ить', 'тьб', 'ьбю', 'жэё']


#  Создаем свои ошибки
class PasswordError(Exception):
    pass


class LengthError(PasswordError):
    pass


class LetterError(PasswordError):
    pass


class DigitError(PasswordError):
    pass


class SequenceError(PasswordError):
    pass


#  Класс для проверки надежности пароля
class CheckPassword:
    def __init__(self, password):
        self.password = password
        self.check_password()

    def check_password(self):
        if len(self.password) <= 8:
            raise LengthError
        lower_flag = False
        upper_flag = False
        digit_flag = False
        for w in self.password:
            if w in string.ascii_lowercase or w in RUS_LOWER:
                lower_flag = True
            elif w in string.ascii_uppercase or w in RUS_UP:
                upper_flag = True
            elif w in string.digits:
                digit_flag = True
        if not lower_flag or not upper_flag:
            raise LetterError
        elif not digit_flag:
            raise DigitError
        flag = CheckPassword.keyboard_check(self)
        if not flag:
            raise SequenceError

    #  Проверяет наличие в пароле запрещенных комбинаций клавиш
    def keyboard_check(self):
        password = self.password.lower()
        flag = True
        for el in combinations:
            if el in password or el[::-1] in password:
                flag = False
                break
        return flag
