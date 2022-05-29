import random

word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
chosen_word_lenght = len(chosen_word)
display = []
print(f"psst, the solution is {chosen_word}")
for _ in chosen_word:
    display.append("_")
end_of_game = False
lives = 6

while end_of_game == False or lives == 1:
    userinput = input("enter a letter").lower()

    for position in (range(len(chosen_word))):
        letter = chosen_word[position]
        if letter == userinput:
            display[position] = letter
    print(display)
    # if userinput != chosen_word_lenght`:
    #     lives -= 1
    #     print(f"you have {lives} remaining")

    if "_" not in display:
        end_of_game = True
        print("you win")
    if lives == 0:
        end_of_game = True
        print("you lose")
