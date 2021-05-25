class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size


def union(llist_1, llist_2):
    node1 = llist_1.head
    node2 = llist_2.head
    union_list = LinkedList()
    items = set()

    while node1:
        items.add(node1.value)
        node1 = node1.next
    while node2:
        items.add(node2.value)
        node2 = node2.next

    if len(items) == 0:
        return None

    for item in items:
        union_list.append(item)

    return union_list


def intersection(llist_1, llist_2):
    node1 = llist_1.head
    node2 = llist_2.head
    inter_list = LinkedList()
    items_1 = set()
    items_2 = set()

    while node1:
        items_1.add(node1.value)
        node1 = node1.next
    while node2:
        items_2.add(node2.value)
        node2 = node2.next

    intersection_set = items_1.intersection(items_2)  # Set intersection() Method

    if len(intersection_set) == 0:
        return None

    for item in intersection_set:
        inter_list.append(item)

    return inter_list


# Test case 1 ================================================================

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print(union(linked_list_1, linked_list_2))
print(intersection(linked_list_1, linked_list_2))


# Test case 2 ================================================================

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_3 = [3,2,4,35,6,65,6,4,3,23]
element_4 = [1,7,8,9,11,21,1]

for i in element_3:
    linked_list_3.append(i)

for i in element_4:
    linked_list_4.append(i)

print(union(linked_list_3,linked_list_4))
print(intersection(linked_list_3,linked_list_4))


# Test case 3 ================================================================

linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_5 = [1,2,3,4,5]
element_6 = [5,4,3,2,1]

for i in element_5:
    linked_list_5.append(i)

for i in element_6:
    linked_list_6.append(i)

print(union(linked_list_5,linked_list_6))
print(intersection(linked_list_5,linked_list_6))


# Test case 4 ================================================================

linked_list_7 = LinkedList()
linked_list_8 = LinkedList()

element_7 = []
element_8 = []

for i in element_7:
    linked_list_7.append(i)

for i in element_8:
    linked_list_8.append(i)

print(union(linked_list_7,linked_list_8))
print(intersection(linked_list_7,linked_list_8))

# Test case 5 ================================================================

linked_list_9 = LinkedList()
linked_list_10 = LinkedList()

element_9 = []
element_10 = [1, 2, 3, 4, 5]

for i in element_9:
    linked_list_9.append(i)

for i in element_10:
    linked_list_10.append(i)

print(union(linked_list_9, linked_list_10))
print(intersection(linked_list_9, linked_list_10))