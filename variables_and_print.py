
# basic string concat with print
character_name = "George"
character_age = "70"
print("There once was a man named " + character_name + ",")
print("he was " + character_age + " years old.")
print("He really liked the name " + character_name + ",")
print("but didn't like being " + character_age + ".")

# for in loop for data-type array
arr = ["Hello ", "there", "!"]
phrase = ""
for word in arr:
  phrase += word
print(phrase)

# data types number and boolean
num = 400
isMale = False

# New Line in string
print("Giraffe\nAcademy")

### Functions ###

phrase2 = "Giraffe Academy"

# convert string to lowercase
print(phrase2.lower())

# convert to upper case
print(phrase2.upper())

# center string in between 100 spaces
print(phrase2.center(100))

# check if string is uppercase
print(phrase2.isupper())

# convert to lowercase and check if string is lowercase
print(phrase2.lower().islower())

# print length of string
print(len(phrase2))

#print 3rd char
print(phrase2[2])

# show index of first occurence of substr "iraff"
print(phrase2.index("iraff"))

# replace element of string
print(phrase2.replace("Giraffe", "Fuck"))

# convert to string
print(str(1 + 5) + " is my favorite number.");

# convert to absolute number 5.5
print(abs(-5.5))

# 10 to the power of 5
print(pow(10, 5))

# return the larger number
print(max(4, 6))

# return min number
print(min(2, 4))

# round number 3.56 to 4
print(round(3.56))

