
def run_lambda():
    add = lambda a, b : a + b
    print (add(1, 2))

def run_list():
    name = "student"
    print (list(name))

def run_set():
    list = set()
    print (list)

# run_lambda()
# run_list()
# run_set()

# that is the spec of python default value of param
# default value of 2nd param will be using the 'list' that was used first time
def run_args(a, list=[]):
    list.append(a)
    print (list)

# run_args(1)
# run_args(2)

# receive tuple and map as function params 
def params(*my_tuple, **my_map):
    print ("tuple:", my_tuple)
    print ("map:", my_map)

params(1,2,3, name="john")

# function annotaion styles
# it is able to check type
def fn_anno1(i):
    return i + 100

def fn_anno2(i: int=9):
    return i + 100

def fn_anno3(i: int=-99) -> int:
    return i + 100

print (fn_anno1(10))
print (fn_anno2())
print (fn_anno3())

# one line syntax
def one_line():
    nums = [x ** 2 for x in range(5)]
    print (nums)

one_line()


