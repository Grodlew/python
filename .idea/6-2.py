class Road:
    def __init__(self, _length, _width):
        mat_mass = _length * _width * 25 * 5 / 1000
        print(f'Необходимо {mat_mass} тонн.')


asphalt = Road(20, 5000)
