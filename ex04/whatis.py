import sys

if len(sys.argv) == 1:
    sys.exit(0)
elif len(sys.argv) > 2:
    raise AssertionError("More than one argument is provided")
    sys.exit(1)


try:
    num = int(sys.argv[1])
    if (num % 2) == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")
except ValueError:
    raise AssertionError("Argument must be an integer")
    sys.exit(1)
