def fruits(*f):
    print("The fruits list ",f)
    for i in f:
        print(i)
fruits("BANANA", "GRAPES", "KIWI","APPLE","MANGO")

def flowers(**fl):
    print("red colour flower", fl["redflower"])
flowers(yellowflower="marrigold",redflower="Rose")