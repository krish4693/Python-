class Arith:
    def read(self):
        self.x=int(input("enter the first number:"))
        self.y=int(input("Enter the second number:"))
    def add(self):
        self.sum=self.x+self.y
    def printer(self):
        print(self.sum)

A=Arith()
A.read()
A.add()
A.printer()        