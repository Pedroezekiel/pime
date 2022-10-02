def sentence(words):
    x = {}
    for i in words:
        if i in x:
            x[i] += 1
        else:
            x[i] = 1
    return x


print(sentence("i am a boy"))


