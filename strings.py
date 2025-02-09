from string import Template

def test_basics():
    var = [0, 1, "hello"]
    print (var, ": different data types in a single array variable")

    triple_q = '''triple qoute'''
    print (triple_q, ": '''triple qoute'''")

    triple_dq = """triple double qoute"""
    print (triple_dq, ': """triple double qoute"""')

    concate = "this_" "will_" "be_" "concatenated_" "without '+' sign"
    print (concate)

    escape = r'line\nNo new line'
    print (escape)

    nums = [0, 1, 2, 3, 4, 5]
    nums[1:100] = [9, 8, 7]
    print (nums)
    nums = []
    print (nums)

# test_basics()

def test_template():
    s = Template("hello $your_name !")
    ret = s.substitute(your_name = "John")
    print (ret)

    s = Template("how are you doing $daytime !")
    #ret = s.substitute("today") # ERROR
    ret = s.safe_substitute()
    print (ret)
    ret = s.safe_substitute(daytime = "today")
    print (ret)


test_template()
