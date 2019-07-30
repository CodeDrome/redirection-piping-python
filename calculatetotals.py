import sys


def main():

    totaldebtors = 0.0
    totalcreditors = 0.0

    for amount in sys.stdin:

        if(int(amount) > 0):

            totaldebtors += int(amount)

        else:

            totalcreditors += int(amount)

    print("Debtors:   {:.2f}".format(totaldebtors))
    print("Creditors: {:.2f}".format(totalcreditors))

    print("totals created", file=sys.stderr)


main()
