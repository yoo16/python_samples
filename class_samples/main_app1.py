# from models.Person import Person
from models.Wizard import Wizard

wizard = Wizard("アリス", "wizard")
# wizard = Person("アリス", "wizard")
# wizard.name = "アリス"
# wizard.job = "Wizard"
# wizard.hp = 30

print(wizard.name)
print(wizard.job)
print(wizard.hp)

warrior = Wizard("ボブ", "warrior")
# warrior = Person("ボブ", "warrior")
# warrior.name = "ボブ"
# warrior.job = "Warrior"
# warrior.hp = 50

wizard.walk("town")
wizard.talk(warrior, "こんにちは")

wizard.attack(warrior)
print(warrior.hp)