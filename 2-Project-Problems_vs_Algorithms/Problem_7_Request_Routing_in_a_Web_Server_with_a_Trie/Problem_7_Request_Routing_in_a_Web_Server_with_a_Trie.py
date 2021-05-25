class RouteTrie:
    def __init__(self, handle):
        self.root = RouteTrieNode()
        self.root.handle = handle

    def insert(self, path, handler):

        array_of_path = self.spliting(path)
        current_node = self.root

        for i in range(len(array_of_path)):

            if array_of_path[i] not in current_node.children:
                current_node.children[array_of_path[i]] = RouteTrieNode()
            current_node = current_node.children[array_of_path[i]]

            if i == len(array_of_path) - 1:
                current_node.handle = handler

    def find(self, path):

        array_of_path = self.spliting(path)
        current_node = self.root

        if len(array_of_path) == 1 and array_of_path[0] == "":
            return current_node.handle

        for path in array_of_path:

            if path in current_node.children:
                current_node = current_node.children[path]
            else:
                return None

        return current_node.handle

    def spliting(self, path):
        split_path = path.split('/')
        if len(split_path)>1 and split_path[-1] == "":
            split_path.pop()
        return split_path


class RouteTrieNode:
    def __init__(self):
        self.handle = None
        self.children = dict()


class Router:
    def __init__(self, handler='not found handler'):
        self.trie = RouteTrie(handler)
        self.handler_error = '404 page not found'

    def add_handler(self, path, handler):
        self.trie.insert(path, handler)

    def lookup(self, path):
        returned_hadler = self.trie.find(path)

        if returned_hadler is None:
            return self.handler_error
        else:
            return returned_hadler

# Testing

# create the router and add a route
router = Router("root handler")
router.add_handler("/home/about", "about handler")

print("Pass" if (router.lookup("/") == 'root handler') else "Fail")
print("Pass" if (router.lookup("/home") == '404 page not found') else "Fail")
print("Pass" if (router.lookup("/home/about") == 'about handler') else "Fail")
print("Pass" if (router.lookup("/home/about/") == 'about handler') else "Fail")
print("Pass" if (router.lookup("/home/about/me") == '404 page not found') else "Fail")
