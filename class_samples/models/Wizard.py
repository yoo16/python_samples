from models.Person import Person

class Wizard(Person):
    def __init__(self, name):
        super().__init__(name)
        self.job = "Wizard"
        self.hp = 30
        self.mp = 20
        self.attackPower = 4
        self.defencePower = 3