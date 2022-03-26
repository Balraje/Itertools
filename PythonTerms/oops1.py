import sys
#Polymorphism: Polymorphism is an ability (in OOP) to use a common interface for multiple forms (data types).
class Parrot:
    def fly(self):
        print("Bird's Can Fly..")

    def swim(self):
        print('Parrot Cannot Swim..')

class Penguin:
    def fly(self):
        print('Penguin cannot Fly..')

    def swim(self):
        print('Penguin can Swim..')

#comman Interface
def flying_test(bird):
    bird.fly()

#instance objects
blu = Parrot()
peggy = Penguin()

#pasing the object
flying_test(blu)
flying_test(peggy)

sys.exit(0)

#Encapsulation: we can restrict access to methods and variables.
# This prevents data from direct modification which is called encapsulation.
class Computer:
     def __init__(self):
         self.__maxprice = 900

     def sell(self):
         print("Selling Price :{}".format(self.__maxprice))

     def setMaxPrice(self,price):
         self.__maxprice = price

c = Computer()
c.sell()

#change the price
c.__maxprice = 1000
c.sell()   #Selling Price :900  will not change---->since __maxprice is a private variable, this modification is not seen on the output.

#using setter function
c.setMaxPrice(1200)
c.sell()


sys.exit(0)

#Inheritance
class Bird:
    def __init__(self):
        print("Bird Ready..")

    def whoisHTis(self):
        print("Bird")

    def swim(self):
        print('Swim Faster')

class Penguin(Bird):
    def __init__(self):
        super().__init__()
        print("Penguin is Ready..")

    def whoisHTis(self):
        print('Penguin')

    def run(self):
        print('Run Faster')

peggy = Penguin()
peggy.whoisHTis()
peggy.swim()
peggy.run()



sys.exit(0)

#adding Methods
class Parrot:
    species = 'bird'
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def sing(self,song):
        return "{} sing {}".format(self.name,song)

    def dance(self):
        return "{} is now dancing".format(self.name)


blu = Parrot("Blu",10)
woo = Parrot("Woo",15)

print(blu.sing('Happpy...'))
print(blu.dance())

print("Blue is a {}".format(blu.__class__.species))
print("Woo is a {}".format(woo.__class__.species))

print("{} is {} years old".format(blu.name,blu.age))
print("{} is {} years old".format(woo.name,woo.age))


sys.exit(0)

#Creating classes
class Parrot:
    species = 'bird'
    def __init__(self,name,age):
        self.name = name
        self.age = age

blu = Parrot("Blu",10)
woo = Parrot("Woo",15)

print("Blue is a {}".format(blu.__class__.species))
print("Woo is a {}".format(woo.__class__.species))

print("{} is {} years old".format(blu.name,blu.age))
print("{} is {} years old".format(woo.name,woo.age))

sys.exit(0)