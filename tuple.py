
def create_tuple():
    my_str = "john"
    print (my_str)

    my_tuple = "john",
    print (my_tuple)

    my_tuple_2 = "allen","pole"
    print (my_tuple_2)

    my_tuple_3 = ("hellen", "nadia")
    print (my_tuple_3)

    # Error : tuple function has to take only one param
    # -------------------------------------------------
    # my_tuple_4 = tuple("coller", "sean")
    # print (my_tuple_4)

    my_tuple_4 = tuple(("coller", "sean"))
    print (my_tuple_4)

def tuple_to_list():
    t = ("hellen", "nadia")
    print (t)
    print (list(t))

# tuple_to_list()
# create_tuple()

def change_tuple():
    x = ([0,1], [2,3])
    x[0][0] = 'changed'     # ok to change because chaing list not tuple itself
    print (x)

    y = (1,2,3)
    y[0] = "can't changed"  # runtime error due to tupel is immutable
    print (y)

change_tuple()

