def mach_zwei(f,arg):
    f(arg)
    f(arg)

def print_zweimal(arg):
    print(arg)
    print(arg)

def mach_vier(arg):
    print_zweimal(arg)
    print_zweimal(arg)

mach_vier('hallo')
