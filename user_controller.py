import datetime

class UserController:
    def __init__(self):
        self.ticket_dict = {0: 'Дата', 1: 'Направление',
                            2: 'Время', 3: 'Тип',
                            4: 'Класс', 5: 'Место'}
        self.now = datetime.datetime.now()

    def show_available_dates(self):
        dates_list = list()

        try:
            with open('data/date.txt', 'r') as f:
                for line in f:
                    dates_list.append(line)

                f.close()
        except:
            print('Ошибка чтения из файла!')

        return dates_list

    def show_available_directions(self):
        directions_list = list()

        try:
            with open('data/direction.txt', 'r') as f:
                for line in f:
                    directions_list.append(line)

                f.close()
        except:
            print('Ошибка чтения из файла!')

        return directions_list


    def show_available_time(self):
        time_list = list()

        try:
            with open('data/time.txt', 'r') as f:
                for line in f:
                    time_list.append(line)

                f.close()
        except:
            print('Ошибка чтения из файла!')

        return time_list


    def show_available_type(self):
        type_list = list()

        try:
            with open('data/type.txt', 'r') as f:
                for line in f:
                    type_list.append(line)

                f.close()
        except:
            print('Ошибка чтения из файла!')

        return type_list

    def show_available_class(self):
        class_list = list()

        try:
            with open('data/class.txt', 'r') as f:
                for line in f:
                    class_list.append(line)

                f.close()
        except:
            print('Ошибка чтения из файла!')

        return class_list

    def show_available_sit(self):
        sit_list = list()

        try:
            with open('data/sit.txt', 'r') as f:
                for line in f:
                    sit_list.append(line)

                f.close()
        except:
            print('Ошибка чтения из файла!')

        return sit_list

    def add_time_to_ticket(self, input):
        try:
            self.ticket_dict.update({2:input})

        except:
            print('Ошибка записи!')

    def add_data_to_ticket(self, input):
        try:
            self.ticket_dict.update({0: input})
        except:
            print('Ошибка записи!')


    def add_direction_to_ticket(self, input):
        try:
            self.ticket_dict.update({1: input})
        except:
            print('Ошибка записи!')

    def add_type_to_ticket(self, input):
        try:
            self.ticket_dict.update({3: input})
        except:
            print('Ошибка записи!')

    def add_class_to_ticket(self, input):
        try:
            self.ticket_dict.update({4: input})
        except:
            print('Ошибка записи!')

    def add_sit_to_ticket(self, input):
        try:
            self.ticket_dict.update({5: input})
        except:
            print('Ошибка записи!')

    def show_ticket(self):
        file_strings = list()

        try:
            with open(f'result/ticket{self.now.day}{self.now.minute}{self.now.second}.txt', 'w') as f:
                for key in self.ticket_dict:
                    f.write(f'{key}:{self.ticket_dict[key]}')

                f.close()

        except:
            print('Ошибка чтения из файла!')