class CustomerDiretory:
  def __init__(self):
    self._directory = BinTree()

  def add(self, customer):
    self._directory.insert_sorted(customer)

  def search_by_last_name(str):
    return self._directory.search_by_key(str)
