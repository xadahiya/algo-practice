def partition(alist, l, r):
    ## choose pivot
    pivot = alist[l]

    i = l+1
    for j in range(i,r):
        # print(j, alist, pivot, i)
        if alist[j] < pivot:
            alist[i], alist[j] = alist[j], alist[i]
            i += 1
    alist[l], alist[i-1] = alist[i-1], alist[l]

    return i-1

def quick_sort(alist, l, r):
    if len(alist[l:r]) < 2:
        return alist
    else:
        print(alist[l:r])
        i = partition(alist, l, r)

        quick_sort(alist, l, i)
        quick_sort(alist, i+1, r)

        return alist

asd = [8,6,7,4,1111,444,5,6665,4,3322,3,44,3,5]
print(quick_sort(asd, 0, len(asd)))
