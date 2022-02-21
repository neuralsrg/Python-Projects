class Person:
    cl_var = 'Hey there'  # Class variable
    __ver = 17  # private variable since the double underscore prefix (we can't call it from anywhere except this class)

    def __init__(self, name):
        self.name = name  # Object variable (owned by each individual object)

    def say_hi(self):
        print('Hi,', self.name)


# swa = Person('Swaroop')
# ser = Person('Serge')

# swa.__class__.cl_var = 'By-by'  # Referring to a class
# print(Person.cl_var)

# todo Inheritance

class Warrior():

    def __init__(self, model, ammo_type):
        self.model = model
        self.ammo_type = ammo_type
        print('The Warrior {} has been summoned'.format(model))

    def warrior_info(self):
        print('Warrior model: "{}"\nAmmo type: "{}"'.format(self.model, self.ammo_type))

    def tell(self):
        print('Hi! I am {}'.format(self.model))


class Jedi(Warrior):

    def __init__(self, model, ammo_type, rang):
        Warrior.__init__(self, model, ammo_type)
        self.rang = rang
        print('Jedi {} has been summoned!'.format(self.model))

    def tell(self):
        print('[JEDI] Hi! I am {}'.format(self.model))


class Sith(Warrior):

    def __init__(self, model, ammo_type, rang):
        Warrior.__init__(self, model, ammo_type)
        self.rang = rang
        print('Sith {} has been summoned!'.format(self.model))

    def tell(self):
        print('[SITH] Hi! I am {}'.format(self.model))


# todo Multiple inheritance

class Car:
    """Superclass."""

    def __init__(self, weight, color):
        self.weight = weight
        self.color = color

    def info(self):
        print('This car is {} kg and has {} color'.format(self.weight, self.color))


class GermanCars:

    def __init__(self):
        self.manufacturer = 'Germany'


class Mercedes(Car, GermanCars):

    def __init__(self, weight, color):
        Car.__init__(self, weight, color)
        GermanCars.__init__(self)

    def tell(self):
        print('This car is from {}. It is {} kg and has {} color'.format(self.manufacturer, \
                                                                         self.weight, self.color))
c1 = Mercedes(1000, 'black')
c1.tell()