def merge_and_count(lefthalf, righthalf):
    # print("Merging", lefthalf, righthalf)
    inversion_count = 0
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
            inversion_count += len(lefthalf[i:])

    while i < len(lefthalf):
        result.append(lefthalf[i])
        i=i+1

    while j < len(righthalf):
        result.append(righthalf[j])
        j=j+1
    return result, inversion_count

def sort_and_count(alist, len_a):
    # print("Splitting ",alist)
    if len(alist) < 2:
        ## Will return sorted list and 0 inversions
        return alist[:], 0
    else:
        mid = len(alist)//2

        lefthalf, x = sort_and_count(alist[:mid], len(alist[:mid]))
        righthalf, y = sort_and_count(alist[mid:], len(alist[mid:]))
        flist, z = merge_and_count(lefthalf, righthalf)

        return flist, (x+y+z)

# alist = [1,3,5,2,4,6]
#text_file = open('integer_array_inversion.txt', 'r')
#alist = [int(a) for a in text_file.read().split("\n") if a != '']
# print(len(alist))
alist = [81, 85, 69, 83, 84, 73, 79, 78]
# print(alist)
print("Result", sort_and_count(alist, len(alist))[1])
