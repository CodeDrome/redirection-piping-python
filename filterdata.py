import sys


def main():

    if(len(sys.argv) > 1):

        try:

            minimum = int(sys.argv[1])

        except ValueError:

            print("Argument must be valid integer", file=sys.stderr)

        for amount in sys.stdin:

            if(abs(int(amount)) >= minimum):

                print(amount, end="")

    else:

        print("minimum must be specified", file=sys.stderr)

    print("data filtered", file=sys.stderr)


main()
