secret_word = "giraffe"
guess = ""
tries = 0

while guess != secret_word and tries < 5:
  guess = input("Guess the secret word: ")
  tries += 1
  if guess == secret_word:
    print("You won")
  elif guess != secret_word and tries < 5:
    print("Wrong word try again")
  else:
    print("You lost")

