
def create_list():
    arr = list(range(5))
    print (f"list={arr}, len={len(arr)}")
    arr1 = list(range(2,10,2))
    print (f"list={arr1}, len={len(arr1)}")

def del_arr():
    number = [1, 2, 3, 4, 5, 6, 7]
    del number[5]
    print (number)

    del number[1:3]
    print (number)

    del number[:]
    print (number)

def pop_append_arr():
    print ("arrays handling with pop/append:")
    numbers = [1, 2, 3, 4, 5, 6, 7]
    new_numbers = []
    while numbers:
        val = numbers.pop()
        new_numbers.append(val)
    print (new_numbers)

def copy_arr():
    print ("copy arrays: ")
    names = ["Sean", "Mike", "Chelsey"]
    new_names = names.copy()
    names.remove("Chelsey")
    print (names)
    print (new_names)
    names.clear()
    print (names)

def search_element():
    str = "0123456"
    print (f"str={str}")
    print (f"str[0]={str[0]}")
    print (f"str[-1]={str[-1]}")
    print (f"str[1:3]={str[1:3]}")

def slice_operator():
    str = "0123456"
    print (f"str={str}")
    print (f"str[1:6:2]={str[1:6:2]}")
    print (f"str[:3]={str[:3]}")
    print (f"str[3:]={str[3:]}")
    print (f"str[:]={str[:]}")
    print (f"str[::2]={str[::2]}")
    print (f"str[::2]={str[::-1]}")

#
# list.index(seach, start, stop)
#
def index_method():
    numbers = [5, 3, 5, 1, 3, 2, 4, 3, 4, 3]
    print (numbers.index(3))
    print (numbers.index(3, 2))
    print (numbers.index(3, 5, 9))

    names = ["sean", "patty", "john"]
    print (names.index("patty"))
    
# create_list()
# del_arr()
# pop_append_arr()
# copy_arr()
# search_element()
# slice_operator()
index_method()
