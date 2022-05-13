from user import User
from worker import Worker

user = User()
worker = Worker()

def login(input):
    if input == '1':
        user.user()

    elif input == '2':
        worker.worker()

    elif input == '3':
        return -1


if __name__ == '__main__':
    while True:
        message = input('В какой интерфейс хотели бы войти?\n'
              '1: Пользователь\n'
              '2: Работник\n'
              '3: Выход\n\n'
              'Для выбора - введите число\n')

        if message == '3' or message == 'выход':
            break

        login_profile = login(message)

        if login_profile == -1:
            break




