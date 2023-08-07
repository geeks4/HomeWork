class SuperHero:
   people='people'
   def __init__(self,name,nickname,superpower,health_points,catchphrase,):
    self.name=name
    self.nickname=nickname
    self.superpower=superpower
    self.health_points=health_points
    self.cathphrase=catchphrase
    self.print_name()
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