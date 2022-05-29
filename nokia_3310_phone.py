phone_menu = """1 -->  Phone Book
2 -->  Message
3 -->  Chat
4 -->  Call Register
5 -->  Tones
6 -->  Settings
7 -->  Call Divert
8 -->  Games
9 -->  Calculator
10 --> Reminders
11 --> Clock
11 --> Profiles
12 --> Sim services"""
print(phone_menu)
phone_menu_input = input("ENTER  A NUMBER: ")


# phone_book_input = input("  ")

def phone_book():
    phone_book = """
1 --> Search
2 --> Search Nos.
3 --> Add name
4 --> Erase
5 --> Edit
6 --> Assign tone
7 --> Send b'card
8 --> options
9 --> Speed dials
10 --> Voice tags"""
    return phone_book


def phone_book_options():
    phone_book_options = """1 --> Type of view
2 --> Memory Satus"""
    return phone_book_options


def message():
    message = """1 --> Write a message
2 --> inbox
3 --> outbox
4 --> Picture message
5 --> Templates
6 --> Smileys"""
    return message


if phone_menu_input == "1":
    print(phone_book())
    phone_book_options_input = input("Enter a number")
    if phone_book_options_input == "8":
        print(phone_book_options())
    else:
        print()
elif phone_menu_input == "2":
    print(message())
