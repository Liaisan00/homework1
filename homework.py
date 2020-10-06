
class Birds():
    food = ("Птичий корм")
    eggs = 'яйца'
    def feed(self):
        self.feed = self.food
    def collect(self):
        self.collect = self.eggs

class Goose(Birds):
    voice = "Га-га-га"
    def __init__(self, name=" ", weight=0):
        self.name = name
        self.weight = weight

class Chicken(Birds):
    voice = "Ко-ко-ко"
    def __init__(self, name=" ", weight=0):
        self.name = name
        self.weight = weight

class Duck(Birds):
    voice = "Кря-кря"
    def __init__(self, name=" ", weight=0):
        self.name = name
        self.weight = weight


class Animals():
    food = ("Трава")
    def feed(self):
        self.feed = self.food

class Cow(Animals):
    voice = "Му"
    milk = 'молоко'
    def __init__(self, name=" ", weight=0):
        self.name = name
        self.weight = weight
    def milking(self):
        self.milking = self.milk

class Sheep(Animals):
    voice = "Ме"
    def __init__(self, name=" ", weight=0):
        self.name = name
        self.weight = weight
    def cut(self):
        self.cut = self.wool

class Goat(Animals):
    voice = "Бе"
    def __init__(self, name=" ", weight=0):
        self.name = name
        self.weight = weight




Goose1 = Goose("Серый", 4)
Goose2 = Goose("Белый", 3)
Cow1 = Cow("Манька", 30)
Sheep1 = Sheep("Барашек", 5)
Sheep2 = Sheep("Кудрявый", 6)
Chicken1 = Chicken("Ко-ко", 2)
Chicken2 = Chicken("Кукареку", 1.5)
Goat1 = Goat("Рога", 6)
Goat2 = Goat("Копыта", 8)
Duck1 = Duck("Кряква", 3)

animals = [Goat1, Goat2, Cow1, Sheep1, Chicken1, Chicken2, Goose1, Goose2, Duck1]
#
# for animal in animals:
    # print(animal.name, animal.weight)
    # print(f'Общий вес {sum([i.weight for i in animals])} кг.')


#я не смогла сделать через список, поэтому сделала через словарь. Если подскажете, как сделать через список,
#буду благодарна. Спасибо

farm = {"Серый":4, "Белый":3, "Манька":30, "Барашек":5, "Кудрявый":6, "Ко-ко":2,"Кукареку":1.5, "Рога":6, "Копыта":8, "Кряква":3}

x = 0
max_weight = 0

for animal in farm:
    if farm[animal] > x:
        x = farm[animal]
        heaviest = {animal: farm[animal]}
        max_weight = animal
print(f' Самое тяжелое животное {max_weight}' )














