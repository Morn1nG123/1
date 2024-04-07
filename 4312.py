import random

class HealthError(Exception):
    pass

class MoodError(Exception):
    pass

class MoneyError(Exception):
    pass

class Person:
    def __init__(self, name, health=0, mood=0, money=0):
        self.name = name
        self.health = health
        self.mood = mood
        self.money = money

    def __str__(self):
        return f'=== {self.name} ===\n' \
               f'Здоровье: {self.health}\n' \
               f'Настроение: {self.mood}\n' \
               f'Капитал: {self.money}'

    def change_state(self, health=0, mood=0, money=0):
        if self.health + health < 0:
            raise HealthError("Человек скончался")
        if self.mood + mood < 0:
            raise MoodError("Человек впал в депрессию")
        if self.money + money < 0:
            raise MoneyError("Человек обанкротился")

        self.health += health
        self.mood += mood
        self.money += money

class Action:
    def __init__(self, name, health=0, mood=0, money=0):
        self.name = name
        self.health = health
        self.mood = mood
        self.money = money

class Work(Action):
    pass

class Rest(Action):
    pass

def do_action(person, action):
    if type(action) == Work:
        if person.mood > 90:
            person.change_state(money=action.money * 1.1, mood=action.mood, health=action.health)
        else:
            person.change_state(money=action.money, mood=action.mood, health=action.health)
    elif type(action) == Rest:
        if person.health < 40:
            person.change_state(money=action.money, mood=int(action.mood * 0.8), health=action.health)
        else:
            person.change_state(money=action.money, mood=action.mood, health=action.health)
    else:
        person.change_state(money=action.money, mood=action.mood, health=action.health)

actions = [Work(name='Работа', health=-5, mood=-20, money=100),
           Rest(name='Отдых', health=10, mood=15, money=-20)]

people = [Person(name='Тарас', health=100, mood=100, money=0),
          Person(name='Мария', health=80, mood=90, money=50),
          Person(name='Иван', health=70, mood=80, money=100)]

while people:
    person = random.choice(people)
    action = random.choice(actions)
    try:
        do_action(person, action)
    except (HealthError, MoodError, MoneyError) as e:
        print(f"{person.name} вышел из игры: {e}")
        people.remove(person)
    else:
        print(person)



