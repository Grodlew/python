from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def cloth_required(self):
        pass

    @abstractmethod
    def total_cloth_req(self):
        pass


class Coat(Clothes):
    coats_num = []

    def __init__(self, name, size):
        self.size = size
        self.name = name
        self.coats_num.append(self)

    @property
    def cloth_required(self):
        return self.size * 6.5 + 0.5  # формула для пальто с делением дает результат на пару порядков меньше,
        # чем для костюма, что несколько странно)

    def __str__(self):
        return f'{self.name} {self.size} размера потребует {self.cloth_required} ткани'

    @property
    def total_cloth_req(self):
        total = sum([item.cloth_required for item in self.coats_num])
        return f'Всего ткани на пальто: {total}'


class Suit(Clothes):
    suits_num = []

    def __init__(self, name, height):
        self.height = height
        self.name = name
        self.suits_num.append(self)

    @property
    def cloth_required(self):
        return self.height * 2 + 0.3

    def __str__(self):
        return f'{self.name} на рост {self.height} потребует {self.cloth_required} ткани'

    @property
    def total_cloth_req(self):
        total = sum([item.cloth_required for item in self.suits_num])
        return f'Всего ткани на костюмы: {total}'


coat = Coat('Пальто', 48)
coat_2 = Coat('Тренчкот', 54)
suit = Suit('Костюм', 184)
suit_2 = Suit('Смокинг', 172)
print(coat)
print(suit_2)
print(suit.total_cloth_req)
print(coat.total_cloth_req)
