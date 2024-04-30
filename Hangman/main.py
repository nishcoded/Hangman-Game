import random
from ascii_art import game_stages, logo
from word_bank import words_list

print(logo)
random_word = random.choice(words_list)
display = []

#repace letters with blanks
for char in random_word:
    display += "_"
print(display)

lives = 6
game_on = True
while game_on:
    user_guess = input("Guess a letter: ").lower()

    #if the user guesses the same letter again, let them know
    if user_guess in display:
        print(f"You have already guessed {user_guess}.")

    #check guessed letter
    for position in range(len(random_word)):
        letter = random_word[position]

        #if user guesses correct letter
        if user_guess == letter:
            display[position] = letter
            print("Correct Guess!")
            print(display)

    #if user guesses wrong letter
    if user_guess not in random_word:
        print("Incorrect guess!")
        lives -= 1
        print(f"You have {lives} attempts left.")
        if lives == 0:
            game_on = False
            print(f"The correct word was {random_word}. Better luck next time!")
            print("You lose.")

    #check if user guesses all letters correct
    if "_" not in display:
        game_on = False
        print("You win!")

    #print the ASCII art that corresponds to the lives left
    print(game_stages[lives])



