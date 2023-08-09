class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.cathphrase = catchphrase

    def double_health(self):
        self.health_points *= 2

    def __str__(self):
        return (f'Nickname:{self.nickname} \n'
                f'Superpower:{self.superpower} \n'
                f'healthness:{self.health_points}')

    def __len__(self):
        return len(self.cathphrase)

    def print_name(self):
        return f'name: {self.name}'


person = SuperHero('Tim', 'menacing', 'strength', 100, "Evil won't win")

print(str(person))
print(person.print_name())
print(f'catchphrase: {len(person)}')
person.double_health()
print(f'double_health: {person.health_points}')


class Airhero(SuperHero):
    people = 'people'

    def __init__(self, name, nickname, superpower, catchphrase, health_points, damage):
        super().__init__(name, nickname, superpower, catchphrase, health_points)
        self.damage = damage
        self.fly = False

    def multiply_hp(self):
         SuperHero.multiply_hp(self)
         self.health_points **= 2
         self.fly = True

    def fly_true_phrase(self):
        if self.fly:
          print(f'{self.name}: fly in the sky')


person1 = Airhero('josh', 'fast', 'levitating', 'none', 100, 200)
print(person1)
person1.fly_true_phrase()

class Earthhero(SuperHero):
    people = 'people'

    def __init__(self, name, nickname, superpower, catchphrase, health_points, damage):
        super().__init__(name, nickname, superpower, catchphrase, health_points)
        self.damage = damage
        self.fly = False

    def multiply_hp(self):
        self.health_points *= 2
        self.fly = True

    def fly_true_phrase(self):
        if self.fly:
            print(f'{self.name}: fly in the dreams')


person2 = Earthhero('Rick', 'kind', 'fast', 'none', 150, 100)

person2.multiply_hp()
person2.fly_true_phrase()


class Villain(Airhero):
    def __init__(self, name, nickname, superpower, catchphrase, health_points, damage):
        super().__init__(name, nickname, superpower, catchphrase, health_points, damage)
        self.people = 'monster'

    def gen_x(self): ...

    def crit(self,damage):
        return damage ** self.damage


villain = Villain('liam', 'terrifying', 'dark magic', 'none', 350, 350)

villain.fly_true_phrase()
villain.multiply_hp()

another_hero=Airhero
villain_damage = 8
result = villain.crit(villain_damage)

print(result)