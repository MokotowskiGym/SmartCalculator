#  You can experiment here, it won’t be checked

class Plant:
    def __init__(self, variety):
        self.variety = variety
        print("{} is a plant".format(self.variety))


class Cactus(Plant):
    def __init__(self, variety):
        super().__init__(variety)
        print("{} is a cactus".format(self.variety))



opuntia = Cactus("Opuntia")
