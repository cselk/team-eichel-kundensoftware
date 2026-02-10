from leaf import Leaf
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.right = Leaf()
        self.left = Leaf()

    def get_data(self):
        return self.data

    def insert_sorted(self, c):
        if data.is_before(c):
            if left.insert_sorted(c):
                left = TreeNode(c)
        else:
            if right.insert_sorted(c):
                right = TreeNode(c)

    def search_by_key(self, key: str):
        if self.get_data().get_last_name() == key:
            return self.get_data()
        else:
            if self.get_data().is_before_key(key):
                return self.left.search_by_key(key)
            else:
                return self.right.search_by_key(key)
