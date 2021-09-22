
# read: r
# write: w
# append data: a
# read and write: r+

# Open file in read mode
employee_file = open("employees.txt", "r")

# Is file readable?
print("is readable:", employee_file.readable())

# Read whole file
# print("whole file:", employee_file.read())

# Read line --> Not working with prvious print()
#print("readline:", employee_file.readline())

#print("read lines:", employee_file.readlines()[1])


for employee in employee_file.readlines():
  print(employee)

# close file
employee_file.close()