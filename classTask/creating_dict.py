import json


class CustomDict(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __setitem__(self, key, value):
        if key in self:
            raise KeyError(f'Key {key} already exists')
        else:
            super().__setitem__(key, value),
            with (open("my_dict", "w")) as file_obj:
                json.dump(my_dict, file_obj)


# def __getitem__(key):
#     with(open("my_dict","r")) as file_obj:
#         json.load(file_obj)
#         for i in file_obj:
#             if i == key:
#                 pass
# with (open(my_dict, "r")) as file_obj:

# print(__getitem__("key"))


my_dict = CustomDict()
with(open("my_dict","r")) as file_obj:
    print(json.load(file_obj))
    for i,key in file_obj.item():
        print(i)