


class point :

    def __init__(self,num1,num2,num3):
     self.sum = 0   
     self.num1 = num1
     self.num2= num2
     self.num3 = num3
     print("values",self.num1,self.num2,self.num3)

    def sqsum(self,):
     self.num1 = num1 * num1;
     self.num2= num2 * num2;
     self.num3= num3 * num3;
    
     print("SquareSum of values:",self.num1,self.num2,self.num3)
    
    def add_sqsum(self):
      self.sum = self.num1 + self.num2 + self.num3
      print("Sum of no:", self.sum)

num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
num3=int(input("Enter third number: ")) 

obj= point(num1, num2 ,num3)
obj.sqsum ()
obj.add_sqsum ()
print()

