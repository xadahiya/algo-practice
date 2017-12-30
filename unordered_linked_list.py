class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def get_next(self):
        return self.next

    def set_next(self, nxt):
        self.next = nxt

    def get_val(self):
        return self.val

    def __str__(self):
        return str(self.val)


class UnorderedList:
    def __init__(self):
        self.head = None

    def add(self, n):
        temp = Node(n)
        temp.set_next(self.head)
        self.head = temp

    def is_empty(self):
        return self.head == None

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.get_next()

        return count

    def search(self, a):
        current = self.head
        found = False
        while current != None and not found:
            if a == current.get_val():
                found = True
            else:
                current = current.get_next()

        return found

    def remove(self, a):
        current = self.head
        prev = None

        found = False
        while current != None and not found:
            if a == current.get_val():
                found = True
            else:
                prev = current
                current = current.get_next()

        if prev == None:
            self.head = current.get_next()
        else:
            prev.set_next(current.get_next())


mylist = UnorderedList()

mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)

print(mylist.size())
print(mylist.search(93))
print(mylist.search(100))

mylist.add(100)
print(mylist.search(100))
print(mylist.size())

mylist.remove(54)
print(mylist.size())
mylist.remove(93)
print(mylist.size())
mylist.remove(31)
print(mylist.size())
print(mylist.search(93))
