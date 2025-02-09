# ----------------------------------------------------------
#
# Finally
#  - even though exception occured, finally will be performed
#
# Args
#  - When exception occured, the exception params are set as Tuple. Not hashmap
#
# ----------------------------------------------------------
def run_exception(call_back):
    try:
        return call_back()
    except ZeroDivisionError as e:
        print (e)
        print (type(e))
        print (e.args)
    except (NameError, IndexError): 
        print("NameError or IndexError") 
    except ValueError:
        print("ValueError") 
    except Exception as e:
        print ("Exception occured")
        print (e)
    else:
        print ("else")
    finally:
        print ("finally")
    print ("")

def missing_except():
    try:
        raise TypeError("type error", "ng")
    except NameError as e:
        print (e)

def finally_with_return():
    try:
        for i in range(3):
            print (i)
            return
        print ("process done")
    except:
        print ("except")
    finally:
        print ("finally")

def zero_divide():
    print ("run: 5 / 0")
    return (5 / 0)

def invalid_type():
    print ("run: int('abc')")
    return int("abc")

def raise_exception():
    print ("run: raise Exception")
    raise Exception("oh no")

def run_ok():
    print ("ok")

run_exception(zero_divide)
# run_exception(invalid_type)
# run_exception(raise_exception)
# run_exception(run_ok)
# missing_except()
# finally_with_return()

class TestError(Exception):
    # print ("TestError occurred")
    pass

def run_a():
    try:
        run_b()
    except TestError:
        print ("run_a(): exception occurred")

def run_b():
    print ("run_b(): started")
    raise TestError

run_a()

