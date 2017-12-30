def selection_sort(lst):

    for i in range(len(lst)-1, 0, -1):
        max_num = 0
        max_index = 0
        for j in range(i+1):
            if lst[j] > max_num:
                max_num = lst[j]
                max_index = j
        ## Swap numbers
        print(max_num, i)
        lst[i], lst[max_index] = lst[max_index], lst[i]

    return lst

print(selection_sort([3,4,5,683,2,21,3,4,5556]))
