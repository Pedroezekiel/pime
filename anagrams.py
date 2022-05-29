def possible_anagrams(userinput):
    rearranged_anagrams = []
    for i in range(len(userinput)):
        if len(userinput) == 1:
            return rearranged_anagrams.append(userinput[-1])
        else:
            result = possible_anagrams(userinput[:-1])
    return [(ch1 + ch2) for ch1 in rearranged_anagrams for ch2 in userinput]


print(possible_anagrams("boy"))
