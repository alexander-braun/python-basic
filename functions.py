# create func
def say_hi():
  print("Hi")

def end_me():
  print("End of program")

say_hi()
end_me()


def say_hi_to(name, age):
  print("Hello there " + name + ", you are " + str(age))

say_hi_to("Dietrich", 69)


# return keyword
def cube(num):
  return num * num * num
result = cube(4)
print(result)
