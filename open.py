
def open_file(mode):
    file_name = "./test.txt"

    # no need to close if use with method
    with open(file_name, mode) as f:
        f.write("test for writing file \n")

open_file("a")



