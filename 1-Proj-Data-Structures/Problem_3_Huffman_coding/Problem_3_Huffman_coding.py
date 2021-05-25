import sys


class Node:
    def __init__(self, counter, data):
        self.counter = counter
        self.data = data
        self.next = None
        self.left = None
        self.right = None
        self.is_assigned_left = None
        self.is_assigned_right = None
        self.bit = None
        self.is_visited = False
        self.parent = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.num_elements = 0

    def enqueue(self, key, value):
        new_node = Node(key, value)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            self.tail = self.tail.next
        self.num_elements += 1

    def dequeue(self):
        if self.is_empty():
            return None
        value = self.head
        self.head = self.head.next
        self.num_elements -= 1
        return value

    def requeue(self, node):
        if self.head is None:
            self.head = node
        else:
            temp = self.head
            self.head = node
            self.head.next = temp
        self.num_elements += 1

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0


class Tree():
    def __init__(self):
        self.root = None

    def set_root(self, node):
        self.root = node

    def get_root(self):
        return self.root


def frequency_each_character(data):
    # counting the frequency of each character

    array = sorted(list(data))
    dict = {}
    counter = 1

    for i in range(len(array)):
        if i < len(array) - 1:
            if array[i] == array[i + 1]:
                counter += 1
            else:
                dict[array[i]] = counter
                counter = 1
        else:
            dict[array[i]] = counter

    sorted_dict_by_counter = ({k: v for k, v in sorted(dict.items(), key=lambda item: item[1])})

    return sorted_dict_by_counter


def comparing_nodes(current_node, node_1, node_2):
    # left or right child (adding bit)

    if node_2 is None:
        current_node.left = node_1

    elif node_1.counter <= node_2.counter:
        current_node.left = node_1
        current_node.right = node_2

    else:
        current_node.left = node_2
        current_node.right = node_1

    current_node.left.parent = current_node
    current_node.left.next = None
    current_node.left.is_assigned_left = True
    current_node.left.bit = 0

    if node_2 is not None:

        current_node.right.parent = current_node
        current_node.right.next = None
        current_node.right.is_assigned_right = True
        current_node.right.bit = 1

    return current_node


def generate_code_dict(tree):

    code = str()
    start_point = tree.root
    dict = {}

    while start_point:
        if start_point.left is not None and start_point.left.is_visited is False:
            code += str(0)
            start_point = start_point.left

        elif start_point.right is not None and start_point.right.is_visited is False:
            code += str(1)
            start_point = start_point.right

        else:
            if(start_point.data):
                dict[start_point.data] = {"code": code, "frequency": start_point.counter}

            temp = code
            code = temp[:-1]
            start_point.is_visited = True

            if start_point.parent:
                start_point = start_point.parent
            else:
                start_point = None

    return dict


def generate_encoded_data(text, dict):

    encoded_data = ""

    for char in text:
        if char in dict:
            encoded_data += (dict[char]["code"])

    return encoded_data


def huffman_encoding(data):

    if len(data) == 0:
        code = ""
        tree = ""
        return [code, tree]

    dictionary = frequency_each_character(data)
    priority_queue = Queue()
    tree = Tree()

    for key, value in dictionary.items():
        priority_queue.enqueue(value, key)

    while priority_queue.size() > 3:

        node_1 = priority_queue.dequeue()
        node_2 = priority_queue.dequeue()

        merged_node = Node(node_1.counter + node_2.counter, None)
        comparing_nodes(merged_node, node_1, node_2)
        priority_queue.requeue(merged_node)

    if priority_queue.size() <= 3:

        first_node = priority_queue.dequeue()
        second_node = priority_queue.dequeue()
        third_node = priority_queue.dequeue()

        if second_node is None:

            final_node = Node(first_node.counter, None)
            comparing_nodes(final_node, first_node, None)

        elif third_node is None:
            merged_node = Node(second_node.counter, None)
            comparing_nodes(merged_node, second_node, third_node)
            final_node = Node(first_node.counter + merged_node.counter, None)
            comparing_nodes(final_node, first_node, merged_node)

        else:
            merged_node = Node(second_node.counter + third_node.counter, None)
            comparing_nodes(merged_node, second_node, third_node)
            final_node = Node(first_node.counter + merged_node.counter, None)
            comparing_nodes(final_node, first_node, merged_node)

        tree.set_root(final_node)
        dict_code = generate_code_dict(tree)

        # creating encoded data
        code = generate_encoded_data(data, dict_code)
        return ([code, tree])


def huffman_decoding(data, tree):

    to_decode = ""

    if data == "":
        return to_decode

    root = tree.root

    for bit in data:

        if bit == '0' and root.left is not None:
            root = root.left
        elif bit == '1' and root.right is not None:
            root = root.right

        if root.left is None and root.right is None:
            to_decode += root.data
            root = tree.root

    return to_decode


if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))


# test

sentence_1 = "hello World"
encoded_data, tree = huffman_encoding(sentence_1)
decoded_data = huffman_decoding(encoded_data, tree)
print("Pass" if (decoded_data == sentence_1) else "Fail")


sentence_2 = "password incorrect"
encoded_data, tree = huffman_encoding(sentence_2)
decoded_data = huffman_decoding(encoded_data, tree)
print("Pass" if (decoded_data == sentence_2) else "Fail")

sentence_3 = "This is a test"
encoded_data, tree = huffman_encoding(sentence_3)
decoded_data = huffman_decoding(encoded_data, tree)
print("Pass" if (decoded_data == sentence_3) else "Fail")

sentence_4 = ""
encoded_data, tree = huffman_encoding(sentence_4)
decoded_data = huffman_decoding(encoded_data, tree)
print("Pass" if (decoded_data == sentence_4) else "Fail")

sentence_5 = "AAAAAAAAAAAAAAA"
encoded_data, tree = huffman_encoding(sentence_5)
decoded_data = huffman_decoding(encoded_data, tree)
print("Pass" if (decoded_data == sentence_5) else "Fail")
#
sentence_6 = "AAAAAAAAAAbbbbbbb"
encoded_data, tree = huffman_encoding(sentence_6)
decoded_data = huffman_decoding(encoded_data, tree)
print("Pass" if (decoded_data == sentence_6) else "Fail")

