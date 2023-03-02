#importing the regularexpression module
import re
#open the file
file=open("C:\\Users\\vidya\\OneDrive\\Desktop\\logcat_9.txt","r", errors="ignore")

new=open("C:\\Users\\vidya\\OneDrive\\Desktop\\loganalasys.txt","w")
#reading the lines from the given file
res = file.readlines()

for line in res:

    found = re.findall(r'Reboot|Crash|Tombstone', line)
    if found:
        new.write(line)
file.close()
new.close()
'''found=re.search(r'.*Reboot.*|.*Crashes.*|.*Tombstone.*',str(res))
print(len(found))

for lines in found:
    new.write(lines)
file.close()
new.close()
    
    print(line)
    if re.search(r'reboot|crash|tombstone', line):

        new.write(line)


w1=re.findall('.*Reboot.*',str(res))
w2=re.findall('.*Crashes.*', str(res))
w3=re.findall('.*Tombstone.*', str(res))
print(w1,file=new)
print(w2,file=new)
print(w3,file=new)
'''
