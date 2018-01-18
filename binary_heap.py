class BinaryHeap:
    def __init__(self):
        # To start the heap index from 1
        self.items = [0]
        self.count = 0

    def insert(self, a):
        """Insert the item a to the heap."""
        self.count += 1
        self.items.append(a)
        self.bubble_up(self.count)

    def bubble_up(self, i):
        """Try bubbling up the ith element of heap."""
        while i // 2 > 0:
            if self.items[i // 2] > self.items[i]:
                self.items[i // 2], self.items[i] = self.items[i], self.items[i // 2]
                i = i // 2
            else:
                break

    def find_min(self):
        """Return the minimum element from heap."""
        return self.items[1]

    def extract_min(self):
        """Extract the minimum element from the heap."""
        if self.count > 0:
            self.items[1], self.items[-1] = self.items[-1], self.items[1]
            output = self.items.pop()
            self.count -= 1
            self.bubble_down(1)
            return output

    def bubble_down(self, i):
        """Try bubbling down the ith element of heap."""
        while i * 2 < self.count:
            min_index = self.get_min_index(i)
            if self.items[i] > self.items[min_index]:
                self.items[i], self.items[min_index] = self.items[min_index], self.items[i]
            i = min_index

    def get_min_index(self, i):
        """Get index of minimum child node."""
        if i * 2 + 1 > self.count:
            return i * 2
        else:
            if self.items[i * 2] < self.items[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def is_empty(self):
        """Check if heap is empty."""
        return self.count == 0

    def size(self):
        """Return the number of elements in heap."""
        return self.count

    def build_heap(self, alist):
        """build a heap from given list of elements."""
        i = len(alist) // 2
        self.count = len(alist)
        self.items = [0] + alist[:]
        while i > 0:
            self.bubble_down(i)
            i = i - 1

    def __str__(self):
        return (str(self.items))


a = BinaryHeap()
a.build_heap([9, 5, 6, 2, 3])
print(a.extract_min())
print(a.extract_min())
print(a.extract_min())
print(a.extract_min())
print(a.extract_min())
print(a.extract_min())
