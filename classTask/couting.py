from collections import Counter


def list_func(lis):
    list_count = Counter(lis)
    printing_list = []
    x = list_count.most_common()
    for i in x:
        printing_list.append(list(i).pop(0))
    return printing_list
    #    if y > counter:
    #         counter = i
    #     else:
    #        l.append(counter)
    # return l


print(list_func(["h","e","l","l","o"]))


def words(list_of_words):
    from collections import defaultdict
    counter = defaultdict(int)
    for l in list_of_words:
        counter[l] += 1

    return [k for k, _ in sorted(counter.items(), key=lambda x: x[1], reverse=True)]
