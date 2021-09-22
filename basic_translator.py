# Giraffe Language
# vowels -> g

# dog -> dgg
# cat -> cgt

text = input("Input text here: ")
vowels = ["a", "e", "i", "o", "u"]
newText = ""
for letter in text:
  if (letter.lower() in vowels):
    if (letter.islower()):
      newText += "g"
    else:
      newText += "G"
  else:
    newText += letter

print(newText)
