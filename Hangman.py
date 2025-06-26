import random

hangman_stages = [
    """
     -----
     |   |
         |
         |
         |
         |
    =========""",
    """
     -----
     |   |
     O   |
         |
         |
         |
    =========""",
    """
     -----
     |   |
     O   |
     |   |
         |
         |
    =========""",
    """
     -----
     |   |
     O   |
    /|   |
         |
         |
    =========""",
    """
     -----
     |   |
     O   |
    /|\\  |
         |
         |
    =========""",
    """
     -----
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========""",
    """
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    ========="""
]

word_bank = {
    "animals": ["tiger", "zebra", "panda", "eagle", "shark"],
    "fruits": ["apple", "mango", "grape", "peach", "lemon"],
    "colors": ["black", "white", "green", "purple", "brown"]
}

print("Welcome to the Hangman Game")
print("Choose a category:")
for cat in word_bank:
    print("-", cat)

chosen_category = input("Enter your choice: ").strip().lower()
while chosen_category not in word_bank:
    chosen_category = input("Invalid category. Choose again: ").strip().lower()

word = random.choice(word_bank[chosen_category])
guessed = ["_"] * len(word)
guessed_letters = []
wrong_guesses = 0
max_attempts = 6

print("\nGame started")

while wrong_guesses < max_attempts and "_" in guessed:
    print(hangman_stages[wrong_guesses])
    print("\nCategory:", chosen_category.capitalize())
    print("Word:", " ".join(guessed))
    print("Guessed letters:", ", ".join(guessed_letters))
    print("Attempts left:", max_attempts - wrong_guesses)

    guess = input("Guess a letter: ").strip().lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single valid letter\n")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter\n")
        continue

    guessed_letters.append(guess)

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
        print("Correct\n")
    else:
        wrong_guesses += 1
        print("Incorrect\n")

print(hangman_stages[wrong_guesses])
if "_" not in guessed:
    print("\nYou won. The word was:", word)
else:
    print("\nYou lost. The word was:", word)
