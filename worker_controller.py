class WorkerController:
    def __init__(self):
        pass

    def add_date(self):
        res_list = list()
        k = True

        while k==True:
            res = input('Какую дату вы хотели бы добавить?\n')

            res_list.append(res)

            exit_key = input('Хотели бы добавить ещё одну дату?\n'
                             'Да/Нет введите д или н...\n')

            if exit_key == 'Да' or exit_key == 'да' or exit_key == 'д':
                continue

            elif exit_key == 'Нет' or exit_key == 'нет' or exit_key == 'н':
                try:
                    with open('data/date.txt', 'a') as f:
                        for line in res_list:
                            f.write(f'{line}\n')

                        f.close()

                        k = False
                except:
                    print('Ошибка чтения из файла!')

    def add_direction(self):
        res_list = list()
        k = True

        while k==True:
            res = input('Какое направление вы хотели бы добавить?\n')

            res_list.append(res)

            exit_key = input('Хотели бы добавить ещё одно направлене?\n'
                             'Да/Нет введите д или н...\n')

            if exit_key == 'Да' or exit_key == 'да' or exit_key == 'д':
                continue

            elif exit_key == 'Нет' or exit_key == 'нет' or exit_key == 'н':
                try:
                    with open('data/direction.txt', 'a') as f:
                        for line in res_list:
                            f.write(f'{line}\n')

                        f.close()

                        k = False
                except:
                    print('Ошибка чтения из файла!')

    def add_time(self):
        res_list = list()
        k = True

        while k==True:
            res = input('Какое время вы хотели бы добавить?\n')

            res_list.append(res)

            exit_key = input('Хотели бы добавить ещё одно время?\n'
                             'Да/Нет введите д или н...\n')

            if exit_key == 'Да' or exit_key == 'да' or exit_key == 'д':
                continue

            elif exit_key == 'Нет' or exit_key == 'нет' or exit_key == 'н':
                try:
                    with open('data/time.txt', 'a') as f:
                        for line in res_list:
                            f.write(f'{line}\n')

                        f.close()

                        k = False
                except:
                    print('Ошибка чтения из файла!')

    def add_type(self):
        res_list = list()
        k = True

        while k == True:
            res = input('Какой тип вагона вы хотели бы добавить?\n')

            res_list.append(res)

            exit_key = input('Хотели бы добавить ещё один тип?\n'
                             'Да/Нет введите д или н...\n')

            if exit_key == 'Да' or exit_key == 'да' or exit_key == 'д':
                continue

            elif exit_key == 'Нет' or exit_key == 'нет' or exit_key == 'н':
                try:
                    with open('data/type.txt', 'a') as f:
                        for line in res_list:
                            f.write(f'{line}\n')

                        f.close()

                        k = False
                except:
                    print('Ошибка чтения из файла!')

    def add_class(self):
        res_list = list()
        k = True

        while k == True:
            res = input('Какой класс вагона вы хотели бы добавить?\n')

            res_list.append(res)

            exit_key = input('Хотели бы добавить ещё один класс?\n'
                             'Да/Нет введите д или н...\n')

            if exit_key == 'Да' or exit_key == 'да' or exit_key == 'д':
                continue

            elif exit_key == 'Нет' or exit_key == 'нет' or exit_key == 'н':
                try:
                    with open('data/class.txt', 'a') as f:
                        for line in res_list:
                            f.write(f'{line}\n')

                        f.close()

                        k = False
                except:
                    print('Ошибка чтения из файла!')

    def add_sit(self):
        res_list = list()
        k = True

        while k == True:
            res = input('Какое место  вы хотели бы добавить?\n')

            res_list.append(res)

            exit_key = input('Хотели бы добавить ещё одно место?\n'
                             'Да/Нет введите д или н...\n')

            if exit_key == 'Да' or exit_key == 'да' or exit_key == 'д':
                continue

            elif exit_key == 'Нет' or exit_key == 'нет' or exit_key == 'н':
                try:
                    with open('data/sit.txt', 'a') as f:
                        for line in res_list:
                            f.write(f'{line}\n')

                        f.close()

                        k = False
                except:
                    print('Ошибка чтения из файла!')