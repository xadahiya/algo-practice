## With operartor (MIT)
import operator

def merge_with_operator(left, right, compare):
    print("Merging", left, right)
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result


def merge_sort_with_operator(L, compare=operator.gt):
    if len(L) < 2:
        return L[:]
    else:
        print("Splitting", L)
        middle = int(len(L) / 2)
        left = merge_sort_with_operator(L[:middle], compare)
        right = merge_sort_with_operator(L[middle:], compare)
        return merge_with_operator(left, right, compare)

alist = [54,26,93,17,77,31,44,55,20]
print("Result", merge_sort_with_operator(alist))


## Without operator
def merge(lefthalf, righthalf):
    print("Merging", lefthalf, righthalf)
    i=0
    j=0
    result = []
    while i < len(lefthalf) and j < len(righthalf):
        if lefthalf[i] < righthalf[j]:
            result.append(lefthalf[i])
            i=i+1
        else:
            result.append(righthalf[j])
            j=j+1

    while i < len(lefthalf):
        result.append(lefthalf[i])
        i=i+1

    while j < len(righthalf):
        result.append(righthalf[j])
        j=j+1
    return result

def merge_sort(alist):
    print("Splitting ",alist)
    if len(alist) < 2:
        return alist[:]
    else:
        mid = len(alist)//2

        lefthalf = merge_sort(alist[:mid])
        righthalf = merge_sort(alist[mid:])
        return merge(lefthalf, righthalf)

alist = [54,26,93,17,77,31,44,55,20]
print("Result", merge_sort(alist))
