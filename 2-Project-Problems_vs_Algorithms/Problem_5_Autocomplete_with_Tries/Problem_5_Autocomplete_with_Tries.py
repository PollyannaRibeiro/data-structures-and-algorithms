
class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = {}


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current_node = self.root

        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]
        current_node.is_word = True

    def find(self, prefix):
        current_node = self.root

        for char in prefix:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        return current_node.is_word

    def suffixes(self, prefix):
        current_node = self.root
        suffixes_array = []

        for char in prefix:
            if char in current_node.children:
                current_node = current_node.children[char]
            else:
                return []

        def list_suffixes(node, array, accumulator=''):
            if node.is_word:
                array.append(accumulator)
            for char in node.children:
                list_suffixes(node.children[char], array, accumulator + char)

        list_suffixes(current_node, suffixes_array)

        return suffixes_array

# testing


MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)


print("Pass" if (MyTrie.suffixes('an') == ['t', 'thology', 'tagonist', 'tonym']) else "Fail")
print("Pass" if (MyTrie.suffixes('f') == ['un', 'unction', 'actory']) else "Fail")
print("Pass" if (MyTrie.suffixes('tri') == ['e', 'gger', 'gonometry', 'pod']) else "Fail")
print("Pass" if (MyTrie.suffixes('tria') == []) else "Fail")
print("Pass" if (MyTrie.suffixes('he') == []) else "Fail")