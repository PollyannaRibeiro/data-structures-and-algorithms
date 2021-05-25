# Search in a Rotated Sorted Array

Given a sorted array which is rotated at some random pivot point.
Example: `[0,1,2,4,5,6,7]` might become `[4,5,6,7,0,1,2]` 

You are given a target value to search. If found in the array return its index, otherwise return -1.

Assume there are no duplicates in the array and the algorithm's runtime complexity must be in the order of O(log n).

Example:
```
Input: nums = [4,5,6,7,0,1,2], target = 0, Output: 4
```

## Solution

To solve this problem, I created 3 pivots - first, middle and last index. The goal of those pivots are to divide the 
input into segments, and find the orientation of each segment to properly loop over it. It will return -1 if not found.
<br>
Its time complexity is O(log n) and its space complexity is O(n).
- [Rotated Array Search](#Problem_2_rotated_array_search/Problem_2_rotated_array_search.py)
