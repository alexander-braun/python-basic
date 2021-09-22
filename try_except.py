
try:
  # value = 10 / 0
  number = int(input("Enter a number: "))
  print(number)
except ZeroDivisionError as err:
  print("Error!:", err)
except ValueError as err:
  print("Error!:", err)
