# Python Intro - Week 1 Homework
## Revision
Variable is a 'name' assigned to a certain value used to refer to that value. The value assigned to a variable name can be changed at any time.

A variable name must be a single "word", as in there is no space inbetween the characters and it can only contain letters, numbers and underscore '_'.

For example, if you would like to name a variable "student name" it must be written as: `student_name`, `studentName` or `studentname`. 
To assign a variable to a value, use the following syntax: `variableName = "some arbitrary value"`
You can read this as: variableName **is** some arbitrary value.

Some examples of variables being assigned to a value:
- `this_number = 1` : This number IS 1.
- `newest_student_name = "Alice"` : Newest student's name is Alice.
- `shopping_list = ["orange","apple","banana"]`:  Shopping list is orange, apple and banana
## Homework
### Excercise 1
Write a program to add two numbers and print them to the screen.
##### Example:
```
What is x?: 5
What is y?: 11
x + y = 16
```
```
What is x?: 5.5
What is y?: -3
x + y = 2.5
```
### Excercise 2
Write a simple calculator for 2 numbers and print them to the screen with all arithmetic operators.
##### Reminder: 
Python built-in operators:
```
Sum: x + y
Difference: x - y
Product: x * y
Division: x / y
Integer division: x // y
Remainder: x % y
Negative: -x
Absolute value: abs(x)
Power: x ** y
```
##### Example:
```
x : 5
y : 10
x+y = 15
x-y = -5
(Continue with other arithmetics operators)
...
...
...
```

### Excersise 3
Create a currency converter from USD to VND. Given that 1 USD = 23,031.35 VND.
###### Example:
```
Enter amount in USD: 12.5
Amount converted to VND: 287891.88
```

## Extended content:
##### Importing libraries:
Recall that Python has built-in functions such as `print()`, `int()`, `float()` and many more.
In Python, you can import external `libraries` to use their existing functionalities that is not provided with Python by default. For example, if we want to find the sine and cosine of an angle, we have to use the `math` library.
To use functions from a `library` use the following command:
```
import library_name
```
To use the cosine function from `math`: we will need to add the import command on the top of our Python file, then we will need to refer to the `cos` function of that `math` library by using the syntax `library.function_name()`, which in our case is `math.cos()`.
```
import math
cosine_value = math.cos(90)
print("Cosine of 90 =", cosine_value)

>>> Cosine of 90 = -0.4480736161291701
```
**Note**: _The angles used for `math` functions are in radians, which means `math.cos(90)` is the cosine of a 90 radians angle and not 90 degrees. To convert degrees to radians use:_
 $$rad =degrees * \frac{\pi}{180}$$
 So a $90\degree$ angle is equal to $\frac{\pi}{2}$ radians and a $180\degree$ angle is equal to $\pi$ radians.
 Read more about radians angles here: https://www.mathwarehouse.com/trigonometry/radians/convert-degee-to-radians.php

### Excercise 4
Write a program that takes from user input an angle in degrees, print out the radians value and the cosine and sine value of that angle. For $\pi$ you can use `pi = 3.14159265` or `math.pi`.
##### Example
```
>>> Enter angle in degrees: 45
>>> Degrees converted to radians: 0.7853981633974483
>>> Cosine of 45 degrees: 0.7071067811865476
>>> Sine of 45 degrees: 0.7071067811865476
```
```
>>> Enter angle in degrees: 90
>>> Degrees converted to radians: 1.5707963267948966
>>> Cosine of 90 degrees: 6.123233995736766e-17
>>> Sine of 90 degrees: 1.0
```
```
>>> Enter angle in degrees: 180
>>> Degrees converted to radians: 3.141592653589793
>>> Cosine of 180 degrees: -1.0
>>> Sine of 180 degrees: 1.2246467991473532e-16
```
**Note**: _Python uses something called scientific notations, which means `e` stands for powers of 10. So `e-16` means $10^{-16}$ or $\frac{1}{10000000000000000}.$
You would expect the program above to return $\sin{45\degree} = 0$ but instead it gave `1.2246467991473532e-16` $\approx \frac{1}{12200000000000000} \approx 0$. 
This is because computers have limited **precision** when it comes to floats (or a.k.a. floating-point numbers). So when it is calculating floats with many decimal places it has to round the number up or down a bit which results in what we call **rounding error in computers**._

