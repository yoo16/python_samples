class Animal:
    def __init__(self, type, name, crying):
        self.type = type
        self.name = name
        self.crying = crying

    def walk(self):
        message = self.name + "が歩いた"
        print(message)

    def cry(self):
        print(self.crying)

    def escape(self):
        message = self.name + "が逃げた"
        print(message)