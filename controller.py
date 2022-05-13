class Controller:
    def __init__(self):
        pass

    def choose_date(self):
        dates_list = list()

        try:
            with open('data/date.txt', 'r') as f:
                for line in f:
                    dates_list.append(line)

                f.close()
                return dates_list

        except:
            print('Ошибка чтения из файла!')