queue_list = [1, 2, 4, 5, 7, 6]


def add_to_queue():
    x = int(input())
    queue_list.insert(0, x)
    return queue_list


def remove_from_queue():
    queue_list.pop(-1)
    return queue_list

for i in range(10):
    print(add_to_queue())
    print(remove_from_queue())
