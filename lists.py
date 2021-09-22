# create a list
friends = ["kevin", "karen", "jim"]

# access element
print(friends[0])

# get elements 1-end
print(friends[1:])

# get range index 0 and 1
print(friends[0:2])

# modify
friends[0] = "MR Fuck"

# List funcs #

numbers = [4, 8, 15, 16, 23, 42, 1, 0, 20, -50]
names = ["Kevin", "Karen", "Jim", "Oscar", "Timmothy", "Jim"]

# append item with spread operator
print("Names and numbers with spread operator: ", [*names, *numbers])

# append item with .extend()
names.extend(numbers) ### -> ["Kevin", ..., 4, 8...]
print(names)

# extend
names.append([4, 5]) ### -> ["Kevin",..., [4, 5]]
print(names)

# insert
names.insert(1, "Inserted Thing")
print(names)

# remove first instance of "Jim"
names.remove("Jim")
print(names)

# pop last item
names.pop()
print(names)

# count same element in list
print(names.count("Jim"))

# is value in list?
print("Kevin index: ", names.index("Kevin"))

# sort list (also possible with strings)
numbers.sort()
print(numbers)

# reverse list
numbers.reverse()
print(numbers)

# copy
names2 = names.copy()
print("Original List: ", names)
print("Copy: ", names2)

# remove all elements from list
names.clear();
print(names)

print("End")