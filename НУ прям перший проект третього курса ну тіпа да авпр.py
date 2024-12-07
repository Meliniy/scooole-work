import random

class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True
    def to_stud(self):
        print('*Імпульсивно вчиться*')
        self.progress += 0.12
        self.gladness -= 3
    def to_sleep(self):
        print('*Меліній заснув на парі*')
        self.gladness += 2
    def to_chill(self):
        print('Цілий день грав колобкі і терарію')
        self.progress -= 0.12
        self.gladness += 3
    def is_alive(self):
        if self.progress < -0.5:
            print("Тебе відчислили")
            self.alive = False
        elif self.gladness <= 0:
            print("В студента депресія")
            self.alive = False
        elif self.gladness >= 250:
            print("Він був настільки щасливим що спіткнувся і впав в каналізацію де його забили черепашки ніндзхя тому що виглядав дуже дивно")
            self.alive = False
        elif self.progress > 5:
            print('розвиток пішов')
            self.alive = False
    def end_of_day(self):
        print(f'Щастя {self.gladness}')
        print(f'Прогресс {round(self.progress, 2)}')
    def live(self, day):
        day = 'Day' + str(day) + ' of ' + self.name + 'life'
        print(f'{day :=^50}')
        live_cube = random.randint(1, 3)
        if live_cube == 1:
            self.to_stud()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()
        self.end_of_day()
        self.is_alive()
Meliniy = Student(name='Meliniy')
for day in range(365):
    if Meliniy.alive == False:
        break
    Meliniy.live(day)