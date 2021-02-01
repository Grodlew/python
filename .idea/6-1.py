from time import sleep


class TrafficLight:
    __color = ['красный', 'желтый', 'зеленый']

    def running(self):
        delay = [7, 2, 9]
        for el in range(len(TrafficLight.__color)):
            print(TrafficLight.__color[el])
            sleep(delay[el])


tr_light = TrafficLight()
tr_light.running()
