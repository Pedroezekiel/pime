tel_list = {'2': 'ABC', '3': 'DEF', '4': 'GHI', '5': 'JKL', '6': 'MNO', '7': 'PQRS', '8': 'TUV', '9': 'WXYZ'}


def gen_words_from_numbers(phone_number):
    # 232
    if len(phone_number) == 1:
        return list(tel_list[phone_number[0]])

    else:
        result = gen_words_from_numbers(phone_number[:-1])
    return [(ch1 + ch2) for ch1 in result for ch2 in tel_list[phone_number[-1]]]


print(len(gen_words_from_numbers("2323232")))
