# Blockchain

A Blockchain is a sequential chain of records, similar to a linked list. 
Each block contains some information and how it is connected related to the other blocks in the chain. 
Each block contains a cryptographic hash of the previous block, a timestamp, and transaction data. 
For our blockchain, we will be using a SHA-256 hash, the Greenwich Mean Time when the block was created, and text strings as the data.

## Solution

I built a blockchain class that appends blocks on the tail of the chain and also checks if the block is already there. 
The Big O complexity of adding an item is O(1) and the Space Complexity of a linked list is O(n).

