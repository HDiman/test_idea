import random

words = ["рыба", "игра", "слон", "крот", "плющ"]

random_word = random.choice(words)
random_word = list(random_word)
print("Компьютер выбрал слово")
guess = []
for i in range(len(random_word)):
    guess.append('-')
print(guess)

while True:
    user = input("Введите любую букву: ")
    user = user.lower()

    for i in range(len(random_word)):
        if user == random_word[i]:
            guess[i] = user
    print(guess)
    if random_word == guess:
        break
