import random
import words
import art

random_word = random.choice(words.word_list)
print(art.logo)
print("Welcome to Hangman!")
print("The word to guess has", len(random_word), "letters.")
print("You have 6 lives. Good luck!\n")


for letter in random_word:
    print("_", end=" ")

user_guesses = []
lives = 6
print(art.stages[lives])
end_game = False    
while not end_game:
    guess = input("\nGuess a letter: ").lower()

    if guess in user_guesses:
        print(f"You have already guessed the letter '{guess}'. Try again.")
    else:
        user_guesses.append(guess)

        if guess in random_word:
            print(f"Good guess! The letter '{guess}' is in the word.")
        else:
            lives -= 1
            print(f"Wrong guess! The letter '{guess}' is not in the word. You lose a life.")
            print(art.stages[lives])

        display_word = ""
        for letter in random_word:
            if letter in user_guesses:
                display_word += letter + " "
            else:
                display_word += "_ "

        print(display_word.strip())

        if "_" not in display_word:
            end_game = True
            print("Congratulations! You've guessed the word correctly and won the game!")

        if lives == 0:
            end_game = True
            print(f"You've run out of lives. The word was '{random_word}'. Better luck next time!")
