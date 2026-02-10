from treenode import TreeNode


class BinTree:
    def __init__(self, data):
        self.root = TreeNode(data)

    def inser_sorted(self, customer):
        self.root.insert_sorted(customer)

    def search_by_key(self, str):
        return self.root.search_by_key(str)
