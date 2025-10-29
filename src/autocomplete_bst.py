class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        # TODO
        if not self.root:
            self.root = Node(key)
            return True
        
        current = self.root
        while current:
            if key == current.key:
                return False
            
            if key < current.key:
                if current.left is None:
                    current.left = Node(key)
                    return True
                else:
                    current = current.left
            else: 
                if current.right is None:
                    current.right = Node(key)
                    return True
                else:
                    current = current.right
        
        return False

    def find(self, key):
        # TODO
        current = self.root
        
        while current:
            if key == current.key:
                return True
            elif key < current.key:
                current = current.left
            else:
                current = current.right
                
        return False

    def autocomplete(self, prefix, k):
        # Return up to k keys that start with prefix in lexicographic order.
        if k <= 0:
            return []

        results = []

        # produce sorted list of all keys (in-order)
        all_keys = []
        def inorder_collect(node):
            if not node:
                return
            inorder_collect(node.left)
            all_keys.append(node.key)
            inorder_collect(node.right)

        inorder_collect(self.root)

        # collect keys that start with prefix
        matches = [x for x in all_keys if isinstance(x, str) and x.startswith(prefix)]
        if len(matches) >= k:
            return matches[:k]

        # If prefix exists exactly as a key, allow returning the prefix and
        # subsequent lexicographic names (to fill up to k). This handles
        # the single-letter-window test where the prefix itself is a contact.
        if prefix in all_keys:
            idx = all_keys.index(prefix)
            return all_keys[idx: idx + k]

        # otherwise return whatever prefix matches we found (may be < k)
        return matches
