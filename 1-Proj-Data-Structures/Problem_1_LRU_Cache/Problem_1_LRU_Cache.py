# Least Recently Used Cache


class DoubleNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.previous = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, node):
        if self.head is None:
            self.head = node
            self.tail = self.head
            return

        self.tail.next = node
        self.tail.next.previous = self.tail
        self.tail = self.tail.next
        return

    def remove(self):

        to_remove = self.head

        if self.head is not self.tail:

            temp = self.head.next

            self.head.next = None
            self.head = temp
            self.head.previous = None

        else:
            self.head = None
            self.tail = None

        return to_remove

    def move_to_priority(self, node):

        if self.head is not self.tail:
            if self.tail is node:
                return
            if self.head is node:
                temp = self.head
                old_tail = self.tail

                self.head = self.head.next
                self.head.previous = None

                self.tail = temp
                self.tail.next = None
                self.tail.previous = old_tail
                self.tail.previous.next = self.tail

            else:
                temp = node
                old_tail = self.tail

                node.previous.next = node.next
                node.next.previous = node.previous

                self.tail = temp
                self.tail.next = None
                self.tail.previous = old_tail
                self.tail.previous.next = self.tail


class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.capacity = capacity
        self.dictionary = dict()
        self.linked_list = DoublyLinkedList()

    def get(self, key):

        # Retrieve item from provided key. Return -1 if nonexistent.
        if self.capacity <= 0:
            return -1

        if key in self.dictionary:
            self.linked_list.move_to_priority(self.dictionary[key])
            return key
        else:
            return -1

    def set(self, key, value):

        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        if self.capacity <= 0:
            return -1

        if len(self.dictionary) >= self.capacity:
            removed = self.linked_list.remove()
            self.dictionary.pop(removed.key)

        node = DoubleNode(key, value)
        self.linked_list.append(node)
        self.dictionary[key] = node

        return self.dictionary


# Test 1 =====================================================

our_cache = LRU_Cache(5)
our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)

print("Pass" if (our_cache.get(1) == 1) else "Fail")
print("Pass" if (our_cache.get(2) == 2) else "Fail")
print("Pass" if (our_cache.get(9) == -1) else "Fail")

our_cache.set(5, 5)
our_cache.set(6, 6)

print("Pass" if (our_cache.get(3) == -1) else "Fail")


# Test 2 =====================================================

our_cache = LRU_Cache(0)
our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)

print("Pass" if (our_cache.get(1) == -1) else "Fail")
print("Pass" if (our_cache.get(2) == -1) else "Fail")
print("Pass" if (our_cache.get(9) == -1) else "Fail")

our_cache.set(5, 5)
our_cache.set(6, 6)

print("Pass" if (our_cache.get(3) == -1) else "Fail")


# Test 3 =====================================================

our_cache = LRU_Cache(-5)
our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)

print("Pass" if (our_cache.get(1) == -1) else "Fail")
print("Pass" if (our_cache.get(2) == -1) else "Fail")
print("Pass" if (our_cache.get(9) == -1) else "Fail")

our_cache.set(5, 5)
our_cache.set(6, 6)

print("Pass" if (our_cache.get(3) == -1) else "Fail")
