import sys


def main():
    if len(sys.argv) == 1:
        sys.exit(0)

    if len(sys.argv) > 2:
        raise AssertionError("More than one argument is provided")
    try:
        num = int(sys.argv[1])
        if num % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")
    except ValueError:
        raise AssertionError("Argument is not an integer")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"AssertionError: {e}")
