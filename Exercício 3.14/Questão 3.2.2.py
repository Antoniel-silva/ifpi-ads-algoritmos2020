def do_twice(f, a):
    f()
    f()

def print_spam():
    print("spam")

do_twice(print(f))
