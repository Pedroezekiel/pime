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


my_dict = CustomDict()
with(open("my_dict","r")) as file_obj:
    data = json.load(file_obj)
print(data)