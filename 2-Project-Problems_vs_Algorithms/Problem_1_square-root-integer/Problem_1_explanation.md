# Finding the Square Root of an Integer

Find the square root of the integer without using any Python library. You have to find the floor value of the square root.

For example, if the given number is 16, then the answer would be 4.

If the given number is 27, the answer would be 5 because sqrt(5) = 5.196 whose floor value is 5.
The expected time complexity is O(log(n))

## Solution

Firstly,  I separated all the basic cases `sqrt_table` and created a tool to search the sqrt of a given number 
(up to two digits, the sqrt needs to be between 0 and 9). And finally, I calculated the sqrt using the concept 
demonstrated on a FreeCodeCamp [article](https://www.freecodecamp.org/news/find-square-root-of-number-calculate-by-hand/).
<br>
This project was challenging due to the amount of step to calculate the square root.
<br>
The tests were done with different numbers of digits, odd, even numbers, and approximate sqrt.
<br>
The time complexity is Big O(log n) and its Space complexity is O(n).

- [Square Root Integer](#Problem_1_square-root-integer/Problem_1_square-root-integer.py)
