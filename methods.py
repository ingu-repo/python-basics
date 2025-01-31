# count
def run_count():
    colors = ["red", "brown", "blue", "red"]
    print (colors)
    print ("red appeared:", colors.count("red"))

run_count()

# pop : remove always last one
def list_pop():
    colors = ["red", "black", "green", "blue"]
    for color in colors[:]:
        if len(color) > 4:
            print ("before pop", colors)
            colors.pop()
            print ("after pop", colors)
            colors.insert(0, color)
            print ("after insert", colors)

    print(colors)

list_pop()
