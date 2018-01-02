from statistics import median

def find_median_index(lst):
    return lst.index((median(lst)))


def partition(alist, l, r):
    ## choose pivot

    ## If we choose the last element as pivot
    # alist[l], alist[r-1] = alist[r-1], alist[l]

    ## If we choose median as pivot
    # if len(alist[l:r]) %2 == 0:
    #     lst = [alist[l], alist[l + len(alist[l:r])//2 -1], alist[r-1]]
    # else:
    #     lst = [alist[l], alist[l+ (len(alist[l:r])//2 )], alist[r-1]]
    # # print(lst)
    # index = find_median_index(lst)
    #
    # if index == 0:
    #     ## If initial element is median
    #     pass
    # if index == 1:
    #     ## If mid element is median
    #     if len(alist[l:r]) % 2 == 0:
    #         alist[l], alist[l + len(alist[l:r])//2 -1] = alist[l + len(alist[l:r])//2 -1], alist[l]
    #     else:
    #         alist[l], alist[l+ (len(alist[l:r])//2 )] = alist[l+ (len(alist[l:r])//2 )], alist[l]
    # if index == 2:
    #     ## If last element is median
    #     alist[l], alist[r-1] = alist[r-1], alist[l]


    pivot = alist[l]

    i = l+1
    for j in range(i,r):
        # print(j, alist, pivot, i)
        if alist[j] < pivot:
            alist[i], alist[j] = alist[j], alist[i]
            i += 1
    alist[l], alist[i-1] = alist[i-1], alist[l]

    return  i-1



comparisons = 0

def quick_sort_with_comparisons(alist, l, r):
    if len(alist[l:r]) < 2:
        return alist
    else:
        global comparisons
        # print(alist[l:r])
        i = partition(alist, l, r)
        comparisons += len(alist[l:r])-1
        quick_sort_with_comparisons(alist, l, i)
        quick_sort_with_comparisons(alist, i+1, r)

        return alist, comparisons

text_file = open('quick_sort.txt', 'r')
alist = [int(a) for a in text_file.read().split("\n") if a != '']
print(quick_sort_with_comparisons(alist, 0, len(alist))[1])
