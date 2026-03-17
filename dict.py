my_dict = {}

# Dictionary with data
person = {
    "name": "Alaska",
    "age": 23,
    "city": "New York"
}
print(person)

# Dictionary ways to create
scores = dict(math=30, eng=40, sci=35)
print(scores)

# Get values

print(person["name"])
# print(person["job"]) # Not the safer way to identify by keys

# Safer way
print(person.get("job"))

# Add or update
person["email"] = "admin@example.com"
person["age"] = 32

print(person)

# Remove items
del person["email"]  # Remove by keys
age = person.pop("age")  # Remove and return
print(age)
print(person)

person.clear()  # Remove all items
print(person)

# Dictionary methods
person2 = {
    "name": "Bob",
    "age": 43,
    "city": "Toronto"
}

person3 = dict(name="Alice", age=42, city="New York")
print(person2.keys())
print(person3.values())
print(person2.items())

if "name" in person2:
    print("Name attribute found!")

person3.update({"age": 32, "job": "Engineer"})
print(person3)

# Dictionary of Dictionaries
students = {
    "alice": {"age": 12, "grade": "A"},
    "bob": {"age": 14, "grade": "A"},
    "charlie": {"age": 12, "grade": "B"}
}

print(f"Grade of student {next(iter(students))}:-> ",students["alice"]["grade"])


