# File Recursion

For this problem, the goal is to write code for finding all files under a directory (and all directories beneath it) 
that end with a specific suffix.

> `os.walk()` is a handy Python method that can achieve this task very easily. However, for this problem was **NOT** 
allowed to use it.

---

## Solution

I did a loop with recursion that runs for each directory  and file just once, 
so its time and space complexity is O(n). The test also checks for edge cases.

- [File Recursion](#Problem_2_File_Recursion/Proj-File-Recursion.py)
