class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message

class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message
class Car:

    def __init__(self, model, __vin, __numbers):
        self.model = model  #model - название автомобиля (строка)
        self.__vin = __vin  #__vin - vin номер автомобиля (целое число)
        self.numbers = __numbers  #номера автомобиля (строка)
        self.__is_valid_vin(__vin)
        self.__is_valid_numbers(__numbers)

    def __is_valid_vin(self, vin_number):  #принимает vin_number и проверяет его на корректность
        if isinstance(vin_number, int):
            pass
        else:
            raise IncorrectVinNumber('Некорректный тип vin номер')
        if vin_number >= 1000000 and vin_number <= 9999999:
            pass
        else:
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        return

    def __is_valid_numbers(self, numbers):  #принимает number и проверяет его на корректность
        if isinstance(numbers, str):
            pass
        else:
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        if len(numbers) == 6:
            pass
        else:
            raise IncorrectCarNumbers('Неверная длина номера')
        return

try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')
