from leaf import Leaf


class BinTree:
    def __init__(self):
        self.root = Leaf()

    def inser_sorted(self, customer):
        self.root.insert_sorted(customer)

    def search_by_key(self, str):
        return self.root.search_by_key(str)
