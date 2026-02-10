
class Customer:
    def __init__(self, first_name: str, last_name: str, id: int):
        self.first_name = first_name
        self.last_name = last_name
        self.id = id
    
    def get_first_name(self):
        return self.first_name
    
    def get_last_name(self):
        return self.last_name
    
    def is_before(self, c):
        return self.is_before_key(c.get_last_name())
    
    def is_before_key(self, key:str):
        return key < self.last_name
    
    