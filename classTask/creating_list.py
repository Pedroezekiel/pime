class CustomList(list):
    def __getitem__(self, index):
        if index <= 0:
            raise IndexError("Index out of range")
        return super().__getitem__(index - 1)
    def __setitem__(self, index, value):
        if index <= 0:
            raise IndexError("Index out of range")
        return super().__setitem__(index - 1, value)


l = CustomList()
l.append(2)
l.append(8)
l[1] = 3
print(l)
