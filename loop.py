def while_loop():
    a, b = 1, 5
    print ("while")
    while a < 30:
        print (a, end=",")
        a = a + b
    print ()

def range_loop():
    print ("range(5):")
    for i in range(5):
        print (i, end=",")
    print()
    print ("range(1,10,2):")
    for i in range(1,10,2):
        print (i, end=",")
    print ()

while_loop()
range_loop()

