class Horse:
    def __init__(self):
        self.x_distance = 0
        self.sound = 'Frr'
        super().__init__()

    def run(self, dx, dy):
        self.x_distance += dx
        super().fly(dy)


class Eagle:
    def __init__(self):
        self.y_distance = 0
        self.sound = "I train, eat, sleep, and repeat"

    def fly(self, dy):
        self.y_distance += dy


class Pegasus(Horse, Eagle):
    def __init__(self):
        super().__init__()


    def move(self, dx, dy):
        super().run(dx, dy)


    def get_pos(self):
        print((self.x_distance, self.y_distance))


    def voice(self):
        print(self.sound)


#print(Pegasus.mro())
pegasus = Pegasus()

pegasus.get_pos()
pegasus.move(10, 15)
pegasus.get_pos()
pegasus.move(-5, 20)
pegasus.get_pos()

pegasus.voice()