def mach_zwei(f):
    f()
    f()

def print_spam():
    print('spam')

mach_zwei(print_spam)
