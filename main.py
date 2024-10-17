class IncorrectVinNumber(Exception):
    """Класс наследуется от класса Exception"""
    def __init__(self, message: str):
        self.message = message


class IncorrectCarNumbers(Exception):
    """Класс наследуется от класса Exception"""
    def __init__(self, message: str):
        self.message = message


class Car:
    """Класс Car"""
    def __init__(self, model: str, vin: int, numbers: str):
        """Конструктор класса. Проверяет аргументы на корректность
        и создает экземпляр класса"""
        if self.__is_valid_vin(vin) and self.__is_valid_numbers(numbers):
            self.model = model          # название автомобиля (строка)
            self.__vin = vin            # vin номер автомобиля (целое число)
            self.__numbers = numbers    # номера автомобиля (строка)

    @staticmethod
    def __is_valid_vin(vin_number):
        """Приватный метод принимает vin_number и проверяет его на корректность.
        Возвращает True, если корректный, в других случаях выбрасывает
        исключение."""
        if not type(vin_number) is int:
            raise IncorrectVinNumber('Некорректный тип vin номер')
        if 1000000 <= vin_number <= 9999999:
            return True
        else:
            raise IncorrectVinNumber('Неверный диапазон для vin номера')


    @staticmethod
    def __is_valid_numbers(numbers):
        """Приватный метод принимает numbers и проверяет его на корректность.
        Возвращает True, если корректный, в других случаях выбрасывает
        исключение"""
        if not type(numbers) is str:
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        if len(numbers) != 6:
            raise IncorrectCarNumbers('Неверная длина номера')
        return True

if __name__ == '__main__':

    # Пример выполняемого кода:
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