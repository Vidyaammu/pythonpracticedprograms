'''
num = int(input("enter any number"))
if num > 0 :
    print ("Number is Positive")
else:
    print("Number is negative")

num = int(input("enter any number"))
print("positive") if num > 0 else print("Negative")

def positivenegative():
    num = int(input("enter any number"))
    if num > 0:
        print("positive")
    else:
        print("negative")
positivenegative()
'''
class positivenegative:
    def __init__(self):
        print("Example")

    def positive(self):
        num = int(input("enter any number"))
        if num >=0:
            if num == 0:
                print("zero")
            else:
                print("positive")
        else:
            print("negative")
    def negative(self):
        num = int(input("enter any number"))
        if num < 0:
            print("negatve")
        else:
            print("positive")
self = positivenegative()
self.positive()
self.negative()



