def change_locally():
    x = 300
    print(" local", x)


def change_globally():
    global x
    x = 150


x = 200
print("global", x)
change_locally()
print("global", x)
change_globally()
print("global", x)
