import math
import sys


class SqrEq:  # Square equation object: ax^2 + bx + c = 0

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.discr = None  # Discriminant
        self.info = None  # Info about the amount of roots

    def show(self):
        print('The equation is: {}x^2 + ({}x) + ({}) = 0'
              .format(self.a, self.b, self.c))


def parameterize_request(f):
    def wrapped(*args, **kwargs):
        try:
            eq = SqrEq(int(args[1]), int(args[2]), int(args[3]))
            return f(eq, **kwargs)
        except Exception as ex:
            print('Wrong arguments!')
            print(ex)
            return None

    return wrapped


def discriminant(f):
    def wrapper_function(obj):
        d = obj.b ** 2 - 4 * obj.a * obj.c
        obj.discr = d
        obj.show()

        if d < 0:
            obj.info = 'NONE'
            print('D = {}, no real roots'.format(d))
            return None
        elif d == 0:
            obj.info = 'ONE'
            print('D = {}, one real root'.format(d))
        else:
            obj.info = 'TWO'
            print('D = {}, two real roots'.format(d))

        return f(obj)

    return wrapper_function


def print_roots(f):
    def wrapped(*args, **kwargs):
        result = f(*args, **kwargs)
        if 'x' in result:
            print('The equation has one real root:'
                  '\n\tx = {:.4f}'.format(result['x']))
        elif 'x1' in result:
            print('The equation has two real roots:' \
                  '\n\tx1 = {:.4f}\n\tx2 = {:.4f}'.format(result['x1'], result['x2']))
        else:
            print('The equation does not have real roots')
        return None

    return wrapped


@parameterize_request
@discriminant
@print_roots
def solve(obj):
    res = {}

    if obj.info == 'ONE':
        res['x'] = -obj.b / 2 * obj.a
    elif obj.info == 'TWO':
        res['x1'] = (-obj.b + math.sqrt(obj.discr)) / 2 * obj.a
        res['x2'] = (-obj.b - math.sqrt(obj.discr)) / 2 * obj.a

    return res


solve(*sys.argv)