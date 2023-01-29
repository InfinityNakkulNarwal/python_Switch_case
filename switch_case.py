#This user-defined module lets you use switch-case module in python which is not present in python 3.8.10

def switch(a):
    for x in range(len(a)):
        print(a[x])
    try:
        print("Please Enter a number 1 to " + str(len(a)))
        c  = int(input("Enter your choice"))
        c = c -1
        if c < 0:
            print("Zero or negative index not allowed")
            print("Please enter a valid number from 1 to " + str(len(a)) + 'to choose.')
        else:
            b = a[c]
            return b
    except IndexError:
        print("Please enter a valid number from 1 to " + str(len(a) + '\n'))

