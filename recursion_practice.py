def list_sum(numlist):
    """Calculate the sum of numbers in the list recursively."""
    if len(numlist) == 1:
        return numlist[0]
    else:
        return numlist[0] + list_sum(numlist[1:])


# print(list_sum([1,2,3,4,5,56,8]))

def fact(num):
    """Calculate factorial of a number num recursively."""
    if num == 1 or num == 0:
        return 1
    else:
        return num*fact(num-1)

# print(fact(55))

def toStr(num, base):
    """Convert any integer to string with any base between 2 and 16."""
    convertString = "0123456789ABCDEF"
    if num < base:
        return convertString[num]
    else:
        return toStr(num//base, base) + convertString[num%base]

# print(toStr(12347588686,15))

def revStr(s):
    """Return the reverse of a string recursively."""
    if len(s) <= 1:
        return s
    else:
        return revStr(s[1:]) + s[0]

# print(revStr("Hello"))
