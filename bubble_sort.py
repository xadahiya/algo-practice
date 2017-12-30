def bubble_sort(lst):
    done = False
    while not done:
        done = True
        for i in range(1, len(lst)):
            if lst[i-1]> lst[i]:
                lst[i-1], lst[i] = lst[i], lst[i-1]
                done = False
    return lst

print(bubble_sort([1,4,5,74,2,1,1,3,5,53,2,5,3322,4,5,64]))
