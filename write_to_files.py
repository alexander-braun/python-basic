
employee_file = open("employees.txt", "a")
# add employee to file
employee_file.write("\nTim - Banker")
employee_file.close()

# owerwrite complete file
new_employee_file = open("employees.txt", "w")
new_employee_file.write("Alex - Only Dude")
new_employee_file.close()

# create new file
new_file = open("new_file.txt", "w")
new_file.write("Alex - New file dude")
new_file.close()