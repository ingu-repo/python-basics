#
# function param order can be changed when calling out the func 
# 
def greeting(name, age, gender="male"):
    print (f"information: name={name}, age={age}, gender={gender}")

#
# "*" keyword is for tuple
# 
def greeting_list(*params):
    for val in params:
        print (val, end=",")
    print ()

#
# "**" keyword is for map
# 
def greeting_map(**params):
    for k in params.keys():
        print (f"{k}={params.get(k)}")
    print ()
    for v in params.values():
        print (f"{v}")
    print ()

greeting("Pole", 20)
greeting(age=20, name="Pole")
greeting(gender="noanswer", age=20, name="Pole")
greeting_list("Pole", "noanswer")
greeting_map(name="Pole", age=19)
