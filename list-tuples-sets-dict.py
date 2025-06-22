# The purpose of this module is to demonstrate the use of lists, tuples, dictionaries and sets.
# To create, append and delete elements from them and to document my learning journey

list_01 = [10, 20, 30, 40, 50, 60]
print(list_01)

list_01.append(70)
print(list_01)

del list_01[1]
print(list_01)

list_01.remove(50)
print(list_01)

person = {"name":"Uche", "age": 30}
print(person.get("age"))


                # Practice Exercise
# Exercise 1
# Create a list to store names of your favorite fruits.
# Write code to access the second element and print it.

fruits = ["apple", "banana", "grape", "pear"]
print(fruits[1])

# Exercise 2
# Define a dictionary to store information about your favorite book,
# including title, author, and genre.
# Use the method to retrieve the genre.

books = {"title": "thursday's child", "author": "Nap Hill", "genre": "romance"}
print(books.get("genre"))

# Exercise 3
# Write a program to generate a random set of numbers between 1 and ten.
# Use set operations to remove duplicates and display the unique numbers.

random_set = {1, 3, 6, 4, 7, 8, 5, 6, 8, 8, 2}
random_x = {9, 5, 2}

x = random_set.intersection(random_x) # Outputs the similarities in the sets
print(x)

y = list(random_x) # Converts set to a list
print(y)

a = random_set.difference(random_x) # Outputs the difference in the sets
print(a)

b = random_x.union(random_set) # Combine both sets
print(b)

print(sorted(random_set or random_x)) # Printing out an ordered output since sets are unordered