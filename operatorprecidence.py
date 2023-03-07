'''BODMAS, also known as PEMDAS, is an acronym that stands for:

B - Brackets
O - Orders (i.e., Powers and Square Roots, etc.)
D - Division
M - Multiplication
A - Addition
S - Subtraction
'''

a = 2
b = 3
c = 4

# Evaluate the expression according to operator precedence
result = (a + b) * c / b ** 2
'''
According to operator precedence rules, parentheses have the highest precedence, (a + b) is evaluated first.
Next, the multiplication operator * is evaluated, followed by the division operator /. 
Both of these operators have the same precedence level, so they are evaluated left to right. 
Thus, the expression becomes 5 * 4 / b ** 2

the exponentiation operator ** is evaluated, followed by the division operator /. 
The exponentiation operator has a higher precedence level than the division operator, so b ** 2 is evaluated first, 
resulting in the intermediate value of 9. Then, the division operator / is evaluated, 
'''
# Display the result
print(result)

x = 5
y = 10
z = 15

# Evaluate the expression according to operator precedence
result = x + y * z - y / x ** 2

'''x ** 2 is evaluated first, resulting in the intermediate value of 25.
y / x ** 2 is evaluated next, resulting in the intermediate value of 0.4.
y * z is evaluated next, resulting in the intermediate value of 150.
x + y * z is evaluated next, resulting in the intermediate value of 155.
Finally, y / x ** 2 is subtracted from x + y * z'''

# Display the result
print(result)   # Output: 150.0