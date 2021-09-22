is_male = False
is_tall = True

if is_male and is_tall:
  print("Is male and tall")
elif is_male or is_tall:
  print("is male or tall")
elif is_male and not(is_tall):
  print("is male and not tall")
else:
  print("Is not male and not tall")


# comparsions in if statements

def max_num(num1, num2, num3):
  if num1 >= num2 and num1 >= num3:
    return num1
  elif num2 >= num3 and num2 >= num1:
    return num2
  else:
    return num3

print(max_num(3, 5, 6))