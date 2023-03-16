for i in range(10):
    print(i)
    if i == 2:
        break

num = 0
for i in range(10):
    num += 1
    if num == 6:
        break
    print("The num has value:", num)
print("Out of loop")