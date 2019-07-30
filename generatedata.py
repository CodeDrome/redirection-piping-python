import random
import sys


def main():

    for i in range(0, 64):

        print(random.randrange(-100, 100))

    print("data generated", file=sys.stderr)


main()
