# GLOBLE VARIABLES
# Python program showing a use of
# global in nested function

def add():
    x = 15

    def change():
        global x
        x = 20
        print("printing inside the change function")
        print(x)

    print("Before making changing: ", x)
    print("Making change")
    change()
    print("After making change: ", x)


add()
print("value of x", x)



