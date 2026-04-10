apimport random

words = ["apple", "tiger", "chair", "plant", "house"]
word = random.choice(words)

guessed_letters = []
wrong_guesses = 0
max_wrong = 6
display = ["_"] * len(word)

while wrong_guesses < max_wrong and "_" in display:
    print("\nWord:", " ".join(display))
    guess = input("Enter a letter: ").lower()

    if guess in guessed_letters:
        print("Already guessed!")
        continue

    guessed_letters.append(guess)

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess
    else:
        wrong_guesses += 1
        print("Wrong guess! Attempts left:", max_wrong - wrong_guesses)

if "_" not in display:
    print("\n🎉 You Win! The word was:", word)
else:
    print("\n💀 You Lose! The word was:", word)