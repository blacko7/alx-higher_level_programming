#!/usr/bin/python3
def add_arg(argv):
    n = len(argv) - 1
    if n == 0:
        print("{:d}".format(n))
        return
    else:
        i = 1
        add = 0
        while i <= n:
            add += int(argv[i])
            i += 1
        print("{:d}".format(add))


if __name__ == "__main__":
    import sys
    add_arg(sys.argv)
............................................................
vi 4-hidden_discovery.py

#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    # Print sorted name from directory
    for name in sorted(dir(hidden_4)):
        # print only names that do not start with __
        if name[:2] != '__':
            print("{}".format(name))
