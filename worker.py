from worker_controller import WorkerController

class Worker:
    def __init__(self):
        self.controller = WorkerController()

    def worker(self):
        while True:
            res = input('1: Ввод даты поездки \n'
                        '2: Ввод направления поездки\n'
                        '3: Ввод времени отправления\n'
                        '4: Ввод типа поезда\n'
                        '5: Ввод класса поезда\n'
                        '6: Ввод места\n'
                        '7: Выход\n')

            if res == '1':
                self.controller.add_date()
            elif res == '2':
                self.controller.add_direction()
            elif res == '3':
                self.controller.add_time()
            elif res == '4':
                self.controller.add_type()
            elif res == '5':
                self.controller.add_class()
            elif res == '6':
                self.controller.add_sit()
            elif res == '7':
                return
            else:
                print('Неправильный ввод, повторите попытку!')
