#Topic: Polymorphism in Python

class Bird:
    def sound(self):
        print("Bird makes a sound")


class Sparrow:
    def sound(self):
        print("Sparrow chirps")


class Crow:
    def sound(self):
        print("Crow caws")


# Function using polymorphism
def make_sound(bird):
    bird.sound()


# Creating objects
b1 = Bird()
s1 = Sparrow()
c1 = Crow()

make_sound(b1)
make_sound(s1)
make_sound(c1)