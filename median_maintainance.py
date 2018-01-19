import heapq

max_heap = []
min_heap = []


file = open('medianMaintainance.txt', 'r')
alist = [int(a) for a in file.read().split("\n") if a != ""]

medians = [alist[0]]

heapq.heappush(max_heap, -alist[0])
for a in alist[1:]:
    if a < - max_heap[0]:
        heapq.heappush(max_heap, -a)
        if len(max_heap) - len(min_heap) > 1:
            temp = heapq.heappop(max_heap)
            heapq.heappush(min_heap, -temp)
    else:
        heapq.heappush(min_heap, a)
        if len(min_heap) > len(max_heap):
            temp = heapq.heappop(min_heap)
            heapq.heappush(max_heap, -temp)

    medians.append(-max_heap[0])
print(len(medians))
print(sum(medians))
