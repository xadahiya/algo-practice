def insertion_sort(lst):
    for i in range(1, len(lst)):
        replace_index = None
        for j in range(i):
            if lst[i]< lst[j]:
                replace_index = j
                break
        if replace_index is not None:
            temp = lst[i]
            for n in range(i, replace_index, -1):
                lst[n] = lst[n-1]
            lst[replace_index] = temp
    return lst

print(insertion_sort([9,22,32,2,3,5,7,22,3455,53,2]))
