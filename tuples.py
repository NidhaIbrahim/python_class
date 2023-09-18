tuple1 = ( 'cyber', 786, 2.23, 'square', 70.2 )
tinytuple = (171, 'square')

print(tuple1[0])
print(tuple1[1:3])
print(tuple1[::3])
print(tinytuple + tuple1)
print(tinytuple*3)
print(tuple1[-4:])
print(tuple1)

# cannot update tuple
tuple1[2] = 90

