file = open('weighted_sum.txt', 'r')

content = file.readlines()

contents = [tuple(int(a) for a in x.strip().split(" ")) for x in content[1:]]

## Sorting by weight first
contents.sort(key= lambda x: x[0], reverse =  True)

## Sorting by w-l
contents.sort(key= lambda x : x[0] - x[1], reverse = True)


def cal_sum_weighted_ct(alist):
    ct = 0
    ws = 0
    for t in alist:
        ct += t[1]
        ws += ct*t[0]
    return ws

print(cal_sum_weighted_ct(contents))
