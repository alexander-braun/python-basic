# 3 to the power of 7
print(3**7)

def exponent(base, exponent):
  result = 1
  for i in range(exponent):
    result *= base
  return result

print(exponent(3, 7))

def exponenWhile(base, exponent):
  result = 1
  times = 0;
  while (times < exponent):
    result *= base
    times += 1
  return result

print(exponenWhile(3, 7))
