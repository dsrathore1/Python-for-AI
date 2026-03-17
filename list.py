# Creating list
my_lists = []

fruits = ["apple", "banana", "cherry"]

mixed = ["Gelo", 1, 1.4, True, 'M']

# Accessing items
print("List of mixed types :-> ", mixed)
print("Data on index 0 :-> ", fruits[0])
print("Data on last of the list :-> ", fruits[-1])

print("Data range from 0 to index no. 3 :-> ", mixed[0:3])

# Changing List - Lists are mutuable
fruits[0] = "Mongo"
print("Changed the first element apple to mango :-> ", fruits)

fruits.append("kiwi")
fruits.insert(1, "grapes")
fruits.insert(3,"watermelon")
print("Append the element at the end of the list :-> ", fruits)

fruits.remove("banana")  # Remove by value
last = fruits.pop()  # Remove and return last
del fruits[1]  # Remove by Index

print(last)
print(fruits)

# List methods
numbers = [1, 2, 3, 4, 5, 6, 7, 1, 1]
print("Length of the number list :-> ", len(numbers))
print(numbers.count(1))  # 3 occurrence of element 1

numbers.sort() # Sort in place
print(numbers)

numbers.reverse()
print(numbers)

new_list = numbers.copy() # Create a copy
new_list.append(3)

print(new_list)
print(numbers)