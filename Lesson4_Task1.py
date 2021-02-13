import sys

def calc_me(args):
    try:
        h, r, b = map(float, args)
        return((h*r) + b)
    except ValueError:
        print('Invalid parameter(s).')
        return None

print('The employee will get a', calc_me(sys.argv[1:]), 'dollars.')

