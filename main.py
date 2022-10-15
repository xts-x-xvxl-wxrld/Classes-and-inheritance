class Vehicle:
    def __init__(self, name=None, max_speed=None):
        self.name = name
        self.max_speed = max_speed

    def set_name(self, x):
        self.name = x

    def set_speed(self, x):
        self.max_speed = x

    def get_name(self):
        return self.name

    def get_speed(self):
        return self.max_speed

    def __str__(self):
        return 'cars name: '+self.name + ', top speed: '+str(self.max_speed)


class Car(Vehicle):

    def __init__(self, name=None, max_speed=None, number_of_cylinders=None):
        Vehicle.__init__(self, name, max_speed)
        self.name = name
        self.max_speed = max_speed
        self.number_of_cylinders = number_of_cylinders

    def set_name(self, x):
        self.name = x

    def set_speed(self, x):
        self.max_speed = x

    def set_cylinders(self, x):
        self.number_of_cylinders = x

    def get_cylinders(self):
        return self.number_of_cylinders

    def __str__(self):
        return 'cars name: '+self.name+', top speed is: '+str(self.max_speed)+', number of cylinders is: '\
               + str(self.number_of_cylinders)


class Plane(Vehicle):

    def __init__(self, name=None, max_speed=None, engines=None):
        Vehicle.__init__(self, name, max_speed)
        self.name = name
        self.max_speed = max_speed
        self.number_of_engines = engines

    def set_name(self, x):
        self.name = x

    def set_speed(self, x):
        self.max_speed = x

    def set_engines(self, x):
        self.number_of_engines = x

    def get_engines(self):
        return self.number_of_engines

    def __str__(self):
        return 'planes name: '+self.name+', top speed is: '+str(self.max_speed)+', number of engines is: '\
               + str(self.number_of_engines)


myVeh = Vehicle()
myVeh.set_name('Honda')
myVeh.set_speed(180)
print(myVeh.__str__())

myCar = Car()
myCar.set_name('Ford')
myCar.set_speed(230)
myCar.set_cylinders(6)
print(myCar.__str__())

myPlane = Plane()
myPlane.set_name('Concord')
myPlane.set_speed(860)
myPlane.set_engines(2)
print(myPlane.__str__())
