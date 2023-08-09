class SuperHero:
    people = 'people'
    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase
    def display_name(self):
        return f"Hero's name: {self.name}"
    def double_health(self):
        self.health_points *= 2
    def __str__(self):
        return f"Nickname: {self.nickname}\nSuperpower: {self.superpower}\nHealth: {self.health_points}"
    def __len__(self):
        return len(self.catchphrase)
hero = SuperHero('Tim', 'menacing', 'strength', 100, "Evil won't win")
print(hero.display_name())
print(f"Health points before: {hero.health_points}")
hero.double_health()
print(f"Health points after doubling: {hero.health_points}")
print(str(hero))
print(f"Catchphrase length: {len(hero)}")
class AirHero(SuperHero):
    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, fly=False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = fly
    def Health_is_double(self):
        SuperHero.Health_is_double(self)
        self.health_points **= 2
        self.fly=True
    def fly_phrase(self):
        return 'fly in the True_phrase'

class SpaceHero(SuperHero):
    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, fly=False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = fly
    def Health_is_double(self):
        SuperHero.double_health(self)
        self.health_points **= 2
        self.fly=True
    def fly_phrase(self):
        return "Fly in the True_phrase: Yes"


air_hero=AirHero('josh', 'fast', 'levitating', 120, 'none', 200)
space_hero=SpaceHero(name='Jacob',nickname='fearless',superpower='magic',
                     health_points=100, catchphrase='none',damage=70)
class Villain(SpaceHero):
    people = 'monster'

    def gen_x(self):...

    def crit(self, damage):
        return damage ** 2

villain=Villain('liam', 'terrifying', 'dark magic',  350, 'none',damage=350)

print('\n')
print(air_hero)
print(f'HealthPoints before: {air_hero.health_points}')
air_hero.double_health()
print(f'Health points after doubling: {air_hero.health_points}')
print(str(air_hero))
print(f'Catchphrase length: {len(air_hero)}')
print(f'Damage: {air_hero.damage}')
print(f'Fly: {air_hero.fly}')

print('\n')
print(space_hero)
print(f'HealthPoints before: {space_hero.health_points}')
space_hero.double_health()
print(f'Health points after doubling: {space_hero.health_points}')
print(str(space_hero))
print(f'Catchphrase length: {len(space_hero)}')
print(f'Damage: {space_hero.damage}')
print(f'Fly: {space_hero.fly}')

print('\n')
print(villain)
print(f'HealthPoints before: {villain.health_points}')
villain.Health_is_double()
print(f'Health points after doubling: {villain.health_points}')
print(str(villain))
print(f'Catchphrase length: {len(villain)}')
print(f'Damage: {villain.damage}')
print(f'Fly: {villain.fly}')

hero_damage = 50
hero_crit_result = villain.crit(hero_damage)
print(f'Critical damage for hero: {hero_crit_result}')