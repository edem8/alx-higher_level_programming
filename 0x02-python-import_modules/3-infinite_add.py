#!/usr/bin/python3


if __name__ == "__main__":
    import sys
    arg_count = 0
    total = 0

    if len(sys.argv) < 2:
        print("{:d}".format(0))
    else:
        for item in sys.argv:
            arg_count += 1

        for num in range(1, arg_count):
            total += int(sys.argv[num]) 
        print("{:d}".format(total))
