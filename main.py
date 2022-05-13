from controller import Controller

controller = Controller()


def user():
    while True:
        res = input('1: Выбор даты поездки \n'
                    '2: Выбор направления поездки\n'
                    '3: Выбор времени отправления\n'
                    '4: Выбор типа поезда\n'
                    '5: Выбор класса поезда\n'
                    '6: Выбор места\n'
                    '7: Сформировать билет\n')

        if res == '1':
            pass
        elif res == '2':
            pass
        elif res == '3':
            pass
        elif res == '4':
            pass
        elif res == '5':
            pass
        elif res == '6':
            pass
        elif res == '7':
            pass
        else: print('Неправильный ввод, повторите попытку!')


def login(input: str):
    if input == '1':
        pass

    elif input == '2':
        pass

    elif input == '3':
        return -1


if __name__ == '__main__':
    while True:
        message = input('В какой интерфейс хотели бы войти?\n '
              '1: Пользователь\n'
              '2: Работник\n'
              '3: Выход\n\n'
              'Для выбора - введите число\n')

        login_profile = login(message)




