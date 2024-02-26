import random
from replit import clear
from Hangman_art import logo
from Hangman_art import stages
from hangman_word_list import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)


lives = 6

print(logo)

display = []

for _ in range(word_length):
    display += "_"

end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    clear()

    if guess in display:
        print(f"You already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"Your guess {guess} is not in the word. You lose one life!")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose!")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win!")

    print(stages[lives])
