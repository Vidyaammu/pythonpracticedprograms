# using format method
str = "sanity"
a=str.index("a")
x='performed'
testcase=4
print(a)

str2 = "smoke"
# Calling function
str3 = "{} and {} both are functional testing".format(str,str2)
# Displaying result
print(str3)
print("{1} and {0} both are functional testings".format(str,str2))

print("a:{a} b:{b} c:{c}".format(a=5,b="testcases",c=12.4))

print("{2} {1} {0}".format(str,str2,str3))

print('a {b} is a {b} for executing {b}cases'.format(b='test'))

print()