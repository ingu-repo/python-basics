
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


create_tuple()

