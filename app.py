import math, sys

def calc( x ,y,op ):
 if op =='+':
    return x+y
 elif op=='-':
        return x -y
 elif op=='*':
  return x*y
 elif op=='/':
       if y==0:
        print("Can't divide by zero")
       else:
        return x/y
 else:
     print( "Invalid op" )

a= 5
b= 1
operator = "+"
result = calc(a,b,operator)
print(  "The result is:",result)