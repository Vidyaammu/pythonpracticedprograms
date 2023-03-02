import re
string="hi hello how are you"
print(re.findall("[i-s]",string))
print(re.search("hello",string))
print(re.split("\s",string,2))
print(re.sub("\s","2",string))
