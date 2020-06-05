import math, random

powers = {}
results = {}
factorials = {}

def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v


def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """

    if (x, y) in results:
        return results[(x, y)]

    if (x, y) in powers:
        power = powers[(x, y)]
    else:
        power = math.pow(x, y)

    if power in factorials:
        factorial = factorials[power]
    else:
        factorial = math.factorial(power)

    result = factorial // (x + y)
    result %= 982451653

    results[(x, y)] = result

    return result



# slowfun(1, 2)
# print(slowfun(1, 2))
# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
