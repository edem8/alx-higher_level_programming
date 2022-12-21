#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    arg_count = 0

    if len(sys.argv) < 2:
        print("{:d} arguments.".format(0))
    elif len(sys.argv) == 2:
        print("{:d} argument:".format(1))
        print("{:d}: {}".format(len(sys.argv) - 1, sys.argv[1]))
    else:
        for item in sys.argv:
            arg_count += 1
        print("{:d} arguments:".format(arg_count - 1))

        for num in range(1, arg_count):
            print("{:d}: {}".format(num, sys.argv[num]))
