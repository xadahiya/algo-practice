def recursive_mul(x, y):
    """Multiply two numbers recursively."""
    if x < 10 or y < 10:
        return x * y
    else:
        n = max(len(str(x)), len(str(y)))
        n -= n % 2
        nb2 = n // 2

        a,b = divmod(x, 10**nb2)
        c,d = divmod(y, 10**nb2)

        ac = recursive_mul(a, c)
        ad = recursive_mul(a, d)
        bc = recursive_mul(b, c)
        bd = recursive_mul(b, d)

        return (10**n) * ac + (10**nb2) * (ad + bc) + bd

print(recursive_mul(1237777777777777999999999999999999456,654321))

# print(recursive_mul(123478987,888888))
