tel_list = {"A": '0', "B": "1", "C": "2", "D": "3", "E": "4", "F": "5", "G": 6, "H": "7", "I": "8", "J": "9"}


def phone_number_generator(userinput):
    if len(userinput) == 1:
        return list(tel_list[userinput[-1]])
    else:
        result = phone_number_generator(userinput[:-1])
    return [(ch1 + ch2) for ch1 in tel_list for ch2 in userinput]


print(len(phone_number_generator("ABCDEF")))
