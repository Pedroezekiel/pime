def is_orded(word):
    numbers = []
    numbers.extend(word)
    if numbers == sorted(numbers):
        ans = "true"
    else:
        ans = "False"
    return ans


print(is_orded("145612"))
