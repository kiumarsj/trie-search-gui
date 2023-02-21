class TrieNode:
    def __init__(self, c):
        self.data = c
        self.children = []
        self.isEnd = False

    def getChild(self, c):
        if self.children != None:
            for child in self.children:
                if child.data == c:
                    return child
        return None

class Trie:
    def __init__(self):
        self.root = TrieNode('')

    def insert(self, word):
        node = self.root
        for ch in word:
            if node.getChild(ch) == None:
                node.children.append(TrieNode(ch))
            node = node.getChild(ch)
        node.isEnd = True

    def autocomplete(self, prefix):
        node = self.root
        res = []
        for char in prefix:
            node = node.getChild(char)
            if node == None:
                return []
        self.helper(node, res, prefix[:-1])
        return res

    def helper(self, node, res, prefix):
        if node.isEnd:
            res.append(prefix + node.data)
        for child in node.children:
            self.helper(child, res, prefix + node.data)
