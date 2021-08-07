print("Exercise 1")
x=float(input("What is x?:"))
y=float(input("What is y?:"))
print("x+y=", x+y)

print("Exercise 2")
x=int(input("x="))
y=int(input("y="))
print("x+y=", x+y)
print("x-y=", x-y)
print("x*y=", x*y)
print("x/y=", x/y)
print("x/y (Integer division)=", x//y,", remain:",x%y)
print("x^y=", x**y)
print("-x=", -x)
print("-y=", -y)
print("|x|=", abs(x))
print("|y|=", abs(y))

print("Exercise 3")
USD=float(input("Enter amount in USD="))
VND=USD*23031.35 
print("Amount converted to VND", VND)

print("Excercise 4")
x=float(input("Enter angle in degrees:"))
import math
cosine_value = math.cos(x*math.pi/180)
sine_value = math.sin(x*math.pi/180) 
print("Degrees converted to radians:", x*math.pi/180)
print("Cosine of ", x, "degrees:", cosine_value)
print("Sine of ", x, "degrees:", sine_value)

