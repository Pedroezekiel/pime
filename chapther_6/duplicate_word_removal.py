from collections import  Counter
def words(list_of_words):
    word_counter = {}
    for i in sorted(list_of_words.split()):
        if i in word_counter:
            word_counter[i] += 1
        else:
            word_counter[i] = 1
    print(f"{'word':<12}counter")
    for i,y in word_counter.items():
        if y>1:
            print(f"{i:<12}    {y}")


words("i can do i can do all thing")