# Dutch National Flag Problem

Given an input array consisting of only 0, 1, and 2, sort the array in **a single traversal**. 
<br>
It's not allowed to use any sorting function that Python provides.

## Solution

Sorted the array in a single traversal using 3 pivots, the first to check the last zero, 
the second to check and remove from the traversal the last correctly positioned numbers 2, 
and the third to run through the array.
Its time and space complexity is O(n).

