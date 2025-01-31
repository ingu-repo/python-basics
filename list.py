
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
    print ("numbers:", numbers)
    numbers.append(8)
    print ("numbers.append(8):", numbers)
    while numbers:
        val = numbers.pop()
        new_numbers.append(val)
    print ("all numbers poped:", numbers)
    print ("appended to new_numbers:", new_numbers)

    # 2d array due to append array
    numbers.append(new_numbers)
    print ("numbers.append(new_numbers):", numbers) 

    # adding array elements
    numbers.extend(new_numbers)
    print ("numbers.extend(new_numbers):", numbers) 

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
    
def list_2d():
    matrix = [[1,2,3], [4,5,6], [7,8,9]]
    for i in matrix:
        print (i)
    for i in matrix:
        for j in i:
            print (j)

# zip(a, b) : pick out two elements from two list and return them as tuple
def use_zip():
    list1 = [1,2,3]
    list2 = [4,5,6]
    for t in zip(list1, list2):
        print ("t:", t)

def use_list():
    str = "0123456"
    print (list(str))

# use_list()
# use_zip()
# create_list()
# del_arr()
# pop_append_arr()
# copy_arr()
# search_element()
# slice_operator()
# index_method()
# list_2d()

def search_element():
    nums = [0, 1, 2, 3, 4, 5]
    print ("nums:", nums)

    if 10 not in nums:
        print ("10 is not in nums")
    else :
        print ("10 exists in nums")

search_element()
