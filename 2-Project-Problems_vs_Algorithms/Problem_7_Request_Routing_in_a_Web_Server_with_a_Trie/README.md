# HTTPRouter using a Trie

For this exercise, we are going to implement a HTTPRouter like you would find in a typical web server using a 
Trie data structure.

There are many different implementations of HTTP Routers such as regular expressions or simple string matching, 
but the Trie is an excellent and very efficient data structure for this purpose.

The purpose of a HTTP Router is to take a URL path like "/", "/about", or "/blog/2019-01-15/my-awesome-blog-post" 
and figure out what content to return. In a dynamic web server, the content will often come from a block of code 
called a handler.

In addition to a path though, we need to know which function will handle the HTTP request. In a real router, we 
would probably pass an instance of a class like Python's `SimpleHTTPRequestHandler` which would be responsible for 
handling requests to that path. For the sake of simplicity, we will just use a string that we can print out to 
ensure we got the right handler

## Solution

Created a trie, a node for the router. 
Also considered for edge cases, handling error message `404 page not found` and handling extra `/` at the end 
of the path. E.g '/about' and '/about/' should have equal results.
<br>
The Find and Insert methods time complexity is O(1) because the time won't change based on the number of handlers 
stored in the router. 
And it's space complexity is O(n).

