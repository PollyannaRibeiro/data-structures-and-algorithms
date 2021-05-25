# LRU Cache

The goal of this project is to design a data structure known as a Least Recently Used (LRU) cache. 
An LRU cache is a type of cache in which we remove the least recently used entry when the cache memory reaches its limit. 
- In case of a cache hit, get() operation should return the appropriate value.
- In case of a cache miss, get() should return -1.
- While putting an element in the cache, put() / set() operation must insert the element. If the cache is full, removes the least recently used entry first and then insert the element.
All operations must take O(1) time.


## Solution

I built a double-linked list to create the following capabilities, insert, move to the top of the list and 
remove the oldest item of the cache. The Big O complexity for all operations are 0(1), due 
to the fact that I used the best feature of two fundamental data structures, a doubled linked and a hash table, this 
way I could easily find a node given a key, and from that node could quickly move it around in the priority list.

And the space complexity is the capacity of the cache, so it is O(capacity). 
Also included tests to check for edge cases.

 - [LRU Cache](#Problem_1_LRU_Cache/Problem_1_LRU_Cache.py)
