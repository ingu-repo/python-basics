
def run_exception(call_back):
    try:
        return call_back()
    except ZeroDivisionError:
        print ("ZeroDivisionError")
    except NameError: 
        print("NameError") 
    except ValueError:
        print("ValueError") 
    except:
        print ("unknown exception")
    print ("")

def zero_divide():
    print ("run: 5 / 0")
    return (5 / 0)

def invalid_type():
    print ("run: int('abc')")
    return int("abc")

def raise_exception():
    print ("run: raise Exception")
    raise Exception("unknown exception")

run_exception(zero_divide)
run_exception(invalid_type)
run_exception(raise_exception)

print ("Done")
