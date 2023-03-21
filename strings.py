name = "vidyalatha"

print(id(name))
substr = "Once upon A time thEre was a king"

print("my string is ", name)

print("length of the string", len(substr))

print("address of string ", id(name))

print(name[9])

print(name[-1])
#print(name[12])
for i in range(len(name)):
    print(name[i],i)
print("vidyalatha,"* 10)

print("slicing for first:",name[0:3])
print("slicing for first::",name[:3])
print("slicing after 4 loaction:",substr[4:])
print("slicing middle 2 loaction:",name[1:3])
print("enter number")
response=input()
number=int(response)
plusten=number+10
print("combine 10 with given number", plusten,response)
print("my sub string is ",substr)
print("count of a character",substr.count("a"))
print("find the string from a substring",substr.find("there"))
temp=substr.find("there")
end=len((substr))
print("element is",substr[temp:11])
print("find from right",substr.rfind("there"))

print("Print evert thing in lowecase:",substr.lower())
print("print string in uppercase :",substr.upper())
print("print capitalize :",substr.capitalize())
print("all fist word as captial:",substr.title())
print("sawap the case:",substr.swapcase())
substr1="hi how are you"
print("remove spaces form both sides of string :",substr1.strip())
print("remove spaces form left sides of string :",substr1.lstrip())
print("remove spaces form right sides of string :",substr1.rstrip())
date1="30-08-1982"
print("remove the delimiter:",date1.split("-"))
print("Add some space or special character to left side of the string",name.ljust(16,"$"))
print("Add some space or special character to right side of the string",name.rjust(18,"@"))
print("Add some space or special character to  and right side of the string",name.center(14,"*"))
number="1298567"
print("fill zeros at starting of the string:",number.zfill(10))
print("replace old word with new one form string:",substr.replace("Once","long"))
print("replace old word with new one form string:",substr.replace("was",""))
print("replace first old word with new one form string:",name.replace("vidya","viddu"))
print("Joing two strings:","".join(substr ),substr1.rjust(12,"-"),number.lstrip())

length = len(substr)
print("length of string :",length)
print("find a substring form string and report tru or false: ",substr.endswith("string",0,length))

print("substr:",substr)
print("find starting value of the string is same as sub string",substr.startswith("On"))