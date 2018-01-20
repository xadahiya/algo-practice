file = open('2sum.txt', 'r')
num_set = set()
for a in file.read().split("\n"):
    if a != "":
        num_set.add(int(a))

print(len(num_set))

target_range = set()
for i in range(-10000, 10001):
    target_range.add(i)

done = set()
for t in target_range:
    for a in num_set:
        if t-a in num_set and t-a != a:
            num_pairs += 1
            break
    print(t, num_pairs)
