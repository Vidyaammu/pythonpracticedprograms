class calculator:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def addition(self):
        add=self.x+self.y
        print(add)
    def subtraction(self):
        sub=self.x-self.y
        print(sub)
    def multiplication(self):
        mul=self.x*self.y
        print(mul)
    def division(self):
        div=self.x//self.y
        print(div)

cal=calculator(7,4)
n=int(input("enter a number",))

if n==1:
    print("Output:",cal.addition())
elif n==2 :
    print("output:",cal.subtraction())
elif n==3:
    print("output:",cal.multiplication())
elif n==4:
    print("output:",cal.division())
elif n==0:
    print("exit")
else:
    print("invalid action")




