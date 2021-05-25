# Rearrange Array Digits

Rearrange Array Elements so as to form two numbers such that their sum is maximum. 
Return these two numbers. You can assume that all array elements are in the range [0, 9]. 
The number of digits in both the numbers cannot differ by more than 1. It's not allowed to 
use any sorting function that Python provides and the expected time complexity is O(nlog(n)).
<br>
for e.g. `[1, 2, 3, 4, 5]`
<br>
The expected answer would be [531, 42]. Another expected answer can be [542, 31]. 
<br>In scenarios such as these when there is more than one possible answer, return anyone.

## Solution

I used a quick sort to sort the array, then I use the biggest numbers to fill the numeric fields with 
higher order, guaranteeing the biggest number. Its time complexity is O(n) and 
space complexity is O(n).

