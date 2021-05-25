#  Huffman Coding 
Data Compression

The compressed data, in turn, helps to reduce the transmission time from a sender to 
receiver. The sender encodes the data, and the receiver decodes the encoded data. 
As part of this problem, you have to implement the logic for both encoding and decoding.
The Huffman Coding is a lossless data compression algorithm.

Assume that we have a string message `AAAAAAABBBCCCCCCCDDEEEEEE` of 25 characters, 
implement the logic for both encoding and decoding.

## Solution

The solution used a queue and a tree as fundamental data structures. 
Created function to check the frequency of each character, assigning a 
bit (0 or 1) depending on if it is left or right child, generating a dictionary 
with the code, you can do both operation huffman encoding and decoding. The time 
complexity of decoding the Huffman tree is O(log n) and its space complexity is O(n).

