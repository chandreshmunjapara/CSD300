
def zero(a, b, c):
    print(a, b, c)

def one(a, b, c):
    print(2*a, b, c)

def x():
    switcher = {
        0: zero,
        1: one
    }
    switcher[1](1,2,3)

x()