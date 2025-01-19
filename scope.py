#
# nonlocal keyword is for one previous scope variable, NOT for the global one
#
i = 9

def run_f1():
    def run_f2():
        nonlocal i
        i = 1
        print ("i:", i)

    i = 2
    run_f2()
    print ("i:", i)

i = 3
run_f1()
print ("i:", i)