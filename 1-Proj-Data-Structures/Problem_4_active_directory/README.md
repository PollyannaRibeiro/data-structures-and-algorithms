#Active Directory

In Windows Active Directory, a group can consist of user(s) and group(s) themselves. 
We can construct this hierarchy as such. Where User is represented by str representing their ids.

Write a function that provides an efficient look-up of whether the user is in a group.

## Solution

I used recursion to run through it and find the users of each group. Its time and space complexity is O(n).

