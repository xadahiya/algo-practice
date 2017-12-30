
def karatsuba(x, y):
    if x < 10 or y < 10:
        return x * y
    # print("x", math.log10(x))
    # get longest digits
    n = max(len(str(x)), len(str(y)))

    # print("n", n)
    # catch where n is odd
    n -= n % 2
    bn2 = 10 ** (n // 2)
    # print(bn)
    x1, x2 = divmod(x, bn2)
    y1, y2 = divmod(y, bn2)
    # print(x1,x2,y1,y2)
    ac = karatsuba(x1, y1)
    bd = karatsuba(x2, y2)
    # caluclate a+b and c + d subtracting already
    # calculated ac and bd leaving ad + bc
    adbc = karatsuba(x1 + x2, y1 + y2) - ac - bd
    # x . y = 10 ^ n ac + 10^n/2 (ad + bc) + bd
    return ((10 ** n) * ac) + bn2 * adbc + bd

# print(karatsuba(1237779456,654321))
# print(karatsuba(123456, 654321))
print(karatsuba(314159265358979323677768462643383279502884197169399375105820974944592, 2718281828459045235360287471352662497757247093699959574966967627))
print(karatsuba(2718281828459045235360287471352662497757247093699959574966967627, 314159265358979323677768462643383279502884197169399375105820974944592))
