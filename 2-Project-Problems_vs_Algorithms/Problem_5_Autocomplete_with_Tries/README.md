# Building a Trie in Python

A trie is a tree-like data structure that stores a dynamic set of strings. 
Tries are commonly used to facilitate operations like predictive text or 
autocomplete features on mobile phones or web searches.

Before we move into the autocomplete function we need to create a working trie for storing strings.  We will create two classes:
* A `Trie` class that contains the root node (empty string)
* A `TrieNode` class that exposes the general functionality of the Trie, like inserting a word or finding the node which represents a prefix.

## Solution

Created a trie and its node, and checked if there are suffixes of the prefixes passed as argument. 
If it doesn't have any, it returns an empty array `[]`. 
The Find and Insert methods time complexity is O(1) because the time won't change based on the number of nodes stored in the trie. 
And it's space complexity is O(n).
