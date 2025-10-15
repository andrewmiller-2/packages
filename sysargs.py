import sys


def main(argv):
    # Expecting: script name, name, age, location
    if len(argv) < 4:
        print("Please provide your name, age, and location as command line arguments.")
        print("Usage: python sysargs.py <name> <age> <location>")
        return 1

    name = argv[1]
    age = argv[2]
    location = argv[3]

    print('hello my name is ' + name)
    print('I am ' + age + ' years old')
    print('I am from ' + location)


if __name__ == '__main__':
    sys.exit(main(sys.argv))