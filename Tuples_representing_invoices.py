from operator import itemgetter

# def sorted():
#     pass

names = ("Jack newton", "mike newton", "caleb notnewton")


def newtons(items):
    if items.__contains__("newton"):
        return items


print(list(filter(newtons, names)))
