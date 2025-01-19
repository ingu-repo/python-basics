
# calc with different types
def calc_diff_types():
    a = 3.14
    b = 5
    print (a + b)

# 複素数
def calc_complex_number():
    # j is 複素数部
    c = 1 + 2j + 3 + 4j
    print (c)

# create str without new line code
def create_str():
    s = (
"hello"
"my"
"friend"
)
    print (s)

def create_multi_line_str():
    # string with new lines
    # Error case
    # --------------------------------
    # ml = "
    # hello
    # python
    # "

    # Can be fixed by triple quote
    # --------------------------------
    ml = """
hello
python
"""
    print (ml)

# list with []
def run_list():
    l = ["hello", "my", "friend"]
    print (l)

# MAP with {}, items()
def run_map():
    m = {0:"Tom", 1:"Philip"}
    print (m)
    for k,v in m.items():
        print ("k:", k, "v:", v)
    m[1]="sam"
    print ("m[1]:", m[1])

# loop in string
def loop_str():
    name = "johnTrabolta"
    for i in name:
        if i == "T":
            break
        elif i == "t":
            break
        else:
            print (i)

def run_bool():
    print (1 > 4 == (10 - 10))
    print ((1, 16) == (1.0, 16.0))
    print("prog" < "proj" < "python")


# create_str()
run_bool()
