def is_palindrome(word):
    x = []
    y = []
    x.extend(word)
    y.extend(word)
    y.reverse()
    if y == x:
        print("True")
    else:
        print("False")


is_palindrome(input("enter something: "))
