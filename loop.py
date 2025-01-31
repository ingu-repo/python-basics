def loop_while():
    a, b = 1, 5
    print ("while")
    while a < 30:
        print (a, end=",")
        a = a + b
    print ("\n")

def loop_range():
    print ("range(5):")
    for i in range(5):
        print (i, end=",")
    print ("\n")

    print ("range(1,10,2):")
    for i in range(1,10,2):
        print (i, end=",")
    print ("\n")

    print ("range(-3, -13, -3):")
    for i in range(-3, -13, -3):
        print (i, end=",")
    print ("\n")

loop_while()
loop_range()

def loop_map(**m):
    for k in m:
        print (k, "=", m[k])

loop_map(name="john", age=18, city="pp")



