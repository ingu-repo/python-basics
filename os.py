import os

dummy_dir = "dummy"
test_dir = "test_dir"
os.chdir(dummy_dir)
os.system(f"mkdir -p {test_dir}")
os.chdir(test_dir)
curr_path = os.getcwd()
print (curr_path)
# print ("dir(curr_path):", dir(curr_path))
