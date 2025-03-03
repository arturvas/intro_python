from sys import argv

print(argv)
print(type(argv))

position_arg = 0
for arg in argv:
    print(position_arg)
    print(arg)
    print(type(argv))
    position_arg += 1
