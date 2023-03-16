#To print number of vowels in a string
string = "my name is vidya Latha"
vowels = "aeiouAEIOU"
count=0
for char in string:
    if char in vowels:
        count+=1
        print(char)
print(count)