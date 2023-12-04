class Библиотека:
    def __init__(self, название, адрес, город, директор):
        self.название = название
        self.адрес = адрес
        self.город = город
        self.директор = директор

    def информация(self):
        print(f"Название библиотеки: {self.название}")
        print(f"Адрес: {self.адрес}")
        print(f"Город: {self.город}")
        print(f"Директор: {self.директор}")
        print()

class ЧитательскийЗал(Библиотека):
    def __init__(self, название, количество_источников, этаж, кабинет):
        super().__init__("Библиотека", "Улица Пушкина, 10", "Москва", "Иванов Иван Иванович")
        self.название = название
        self.количество_источников = количество_источников
        self.этаж = этаж
        self.кабинет = кабинет

    def информация(self):
        super().информация()
        print(f"Название зала: {self.название}")
        print(f"Количество источников литературы: {self.количество_источников}")
        print(f"Этаж: {self.этаж}")
        print(f"Кабинет: {self.кабинет}")
        print()

class Читатели(Библиотека):
    def __init__(self, фамилия, имя, отчество, место_работы, возраст, пол):
        super().__init__("Библиотека", "Улица Пушкина, 10", "Москва", "Иванов Иван Иванович")
        self.фамилия = фамилия
        self.имя = имя
        self.отчество = отчество
        self.место_работы = место_работы
        self.возраст = возраст
        self.пол = пол

    def информация(self):
        super().информация()
        print(f"Фамилия: {self.фамилия}")
        print(f"Имя: {self.имя}")
        print(f"Отчество: {self.отчество}")
        print(f"Место работы: {self.место_работы}")
        print(f"Возраст: {self.возраст}")
        print(f"Пол: {self.пол}")
        print()


# Создаем экземпляры классов и вызываем методы вывода информации
библиотека = Библиотека("Городская библиотека", "ул. Ленина, 1", "Москва", "Иванов Иван Иванович")
библиотека.информация()

читательский_зал = ЧитательскийЗал("Зал чтения", 100, 2, "Кабинет 203")
читательский_зал.информация()

читатель = Читатели("Иванов", "Иван", "Иванович", "ООО Рога и Копыта", 35, "мужской")
читатель.информация()