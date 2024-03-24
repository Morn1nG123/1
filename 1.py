from random import randint
from Lesson_2.character import Character


class Berserk(Character):
    def __init__(self, name, damage):
        super().__init__(name, damage)

    def attack(self, opponent):
        if randint(1, 10) == 1:
            return 1000
        return super().attack(opponent)


class Assassin(Berserk):
    def __init__(self, name, damage):
        super().__init__(name, damage)

    def attack(self, opponent):
        damage = super().attack(opponent)
        if randint(1, 5) == 1:
            return 1000
        return damage




player1 = Character('Vasya', damage=15)
player1.show_info()

player2 = Assassin('Petya', damage=10)
print(player2)

while player1.is_alive() and player2.is_alive():
    p1_damage = player1.attack(player2)
    print(f'{player1.name} атакував {player2.name} '
          f'і наніс {p1_damage} шкоди.')

    p2_damage = player2.attack(player1)
    print(f'{player2.name} атакувавв {player1.name} '
          f'і наніс {p2_damage} шкоди.')

    print(player1, player2, sep='\n')

print(player1, player2, sep='\n')