class ShoppingCart:
    def __init__(self, limit):
        self.limit = limit
        self.item = []

    def add_item(self, items):
        if len(self.item) < self.limit:
            self.item.append(items)
        else:
            self.item.pop(0)
            self.item.insert(0, items)
   
