from user_controller import UserController

class User:
    def __init__(self):
        self.controller = UserController()

    def user(self):
        while True:
            res = input('1: Выбор даты поездки \n'
                        '2: Выбор направления поездки\n'
                        '3: Выбор времени отправления\n'
                        '4: Выбор типа поезда\n'
                        '5: Выбор класса поезда\n'
                        '6: Выбор места\n'
                        '7: Сформировать билет\n'
                        '8: Выход\n')

            if res == '1':
                dates = self.controller.show_available_dates()

                for element in dates:
                    print(f'{dates.index(element)}:{element} \n')

                date_input = input()

                self.controller.add_data_to_ticket(dates[int(date_input)])

            elif res == '2':
                directions = self.controller.show_available_directions()

                for element in directions:
                    print(f'{directions.index(element)}:{element}\n')

                direction_input = input()

                self.controller.add_direction_to_ticket(directions[int(direction_input)])

            elif res == '3':
                time = self.controller.show_available_time()

                for element in time:
                    print(f'{time.index(element)}:{element}\n')

                time_input = input()

                self.controller.add_time_to_ticket(time[int(time_input)])

            elif res == '4':
                train_type = self.controller.show_available_type()

                for element in train_type:
                    print(f'{train_type.index(element)}:{element}\n')

                type_input = input()

                self.controller.add_time_to_ticket(train_type[int(type_input)])

            elif res == '5':
                train_class = self.controller.show_available_class()

                for element in train_class:
                    print(f'{train_class.index(element)}:{element}\n')

                class_input = input()

                self.controller.add_class_to_ticket(train_class[int(class_input)])

            elif res == '6':
                sit = self.controller.show_available_sit()

                for element in sit:
                    print(f'{sit.index(element)}:{element}\n')

                sit_input = input()

                self.controller.add_sit_to_ticket(sit[int(sit_input)])

            elif res == '7':
                self.controller.show_ticket()

            elif res == '8':
                break

            else:
                print('Неправильный ввод, повторите попытку!')