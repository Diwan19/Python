# varible casting

x = str(3)
print(x)
print(type(x))

y = float(3)
print(y)

# Many values to multiple variables
x, y, z = "orange", 3.3, 5
print(x)
print(y)
print(z)

# one value to multiple variables
x = y = z = "orange"
print(x, y, z)

# UNPACKING A COLLECTION IN PYTHON

Cars = ["SUV", "SEDAN", "HATCHBACK"]
x, y, z = Cars
print(x,y,z)
