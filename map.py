
# duplicated map key not allowed
# -------------------------------------------------
def loop_map():
    users = {"sean":17, "patty":34, "john":61 }
    for k,v in users.items():
        print ("key: " + k, ", value:", v)

# sean will be overriden by last one
# -------------------------------------------------
def override_map():
    users = {"sean":17, "patty":34, "sean":99 }
    for k,v in users.items():
        print ("key: " + k, ", value:", v)

def check_not_in():
    users = {"sean":17, "patty":34, "john":61 }
    print ("sean" not in users.keys())
    print (99 not in users.values())

def create_map_simply():
    m = {i: i*2 -1 for i in [1,2,3]}
    print (m)
    
loop_map()
override_map()
check_not_in()
create_map_simply()

