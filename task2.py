
class Road:
    def __init__(self, _lenght, _width):
        self._lenght = _lenght
        self._width = _width

    def mass(self, _lenght, _width):
        a = _lenght * _width * 25 * 2
        print(f'Для покрытия всего дорожного полотна потребуется: {a} тонн асфальта')
        print(f'Решение: {_lenght}м * {_width}м * 25кг * 2см = {a}т')


Road = Road(5000, 10)
Road.mass(5000, 10)
