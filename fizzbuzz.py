#!/usr/bin/python

def fizzbuzz(n):
    """Iterates from 1 to n, and if the ith number is a multiple of two,
    prints fizz, if a multiple of three prints buzz, if a multiple of both
    prints fizzbuzz, else print the value.
    @param n Number of lines to print.
    """
    for i in range(1, n + 1):
        multiple_of_2 = ((i % 2) == 0)
        multiple_of_3 = ((i % 3) == 0)
        if multiple_of_2 and multiple_of_3:
            print 'fizzbuzz'
        elif multiple_of_2:
            print 'fizz'
        elif multiple_of_3:
            print 'buzz'
        else:
            print i

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser('fizzbuzz', 'fizzbuzz.py n')
    parser.add_argument('n', help='number of lines to print', nargs=1, type=int)
    args = parser.parse_args()
    fizzbuzz(args.n[0])

