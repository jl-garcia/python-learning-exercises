name = "Jose Luis Garcia"
age = 32
weight_in_kilos = 69.2
books = ["Programming with Python", "Scala for dummies", "The clean coder"]
sports = ("running", "soccer", "tennis")
a = 40
b = 30
c = 20
d = 45
jogging_minutes_by_day = [{'Monday', a}, {"Tuesday", b}, {"Wednesday", c}, {"Friday", d}]

# Playing with integer variables
anotherAge = age
print(f"age: {age} - id: {id(age)}")
print(f"anotherAge: {anotherAge} - id: {id(anotherAge)}")

age = 0
print(f"age: {age} - id: {id(age)}")
print(f"anotherAge: {anotherAge} - id: {id(anotherAge)}")

print("-----------------")

# Playing with double variables
new_weight_in_kilos = weight_in_kilos  # it removes decimal digits
print(f"weight_in_kilos: {weight_in_kilos} - id: {id(weight_in_kilos)}")
print(f"new_weight_in_kilos: {new_weight_in_kilos} - id: {id(new_weight_in_kilos)}")
new_weight_in_kilos += 10
print(f"weight_in_kilos: {weight_in_kilos} - id: {id(weight_in_kilos)}")   # keeps its value
print(f"new_weight_in_kilos: {new_weight_in_kilos} - id: {id(new_weight_in_kilos)}")

print("-----------------")

# Playing with string variables
new_name = name
print(f"name: {name} - id: {id(name)}")
print(f"new_name: {new_name} - id: {id(new_name)}")

new_name = "Pepe"
print(f"name: {name} - id: {id(name)}")  # does not change
print(f"new_name: {new_name} - id: {id(new_name)}")

new_name = 'Alfonso'
print(f"new_name: {new_name} - id: {id(new_name)}")

sur_name = name
name = new_name
new_name = "There is not name"
print(f"name: {name} - id: {id(name)}")
print(f"new_name: {new_name} - id: {id(new_name)}")
print(f"sur_name: {sur_name} - id: {id(sur_name)}")

print("-----------------")

# Playing with list variables
print(f"books: {books} - id: {id(books)}")

books[0] = 'Harry Potter'
print(f"books: {books} - id: {id(books)}")

my_others_books = books
books[1] = 'TDD guided by tests'
print(f"books: {books} - id: {id(books)}")
print(f"my_others_books: {my_others_books} - id: {id(my_others_books)}")

my_others_books[2] = 'A random book'
print(f"books: {books} - id: {id(books)}")
print(f"my_others_books: {my_others_books} - id: {id(my_others_books)}")


print("-----------------")

# Playing with list variables
print(f"jogging_minutes_by_day: {jogging_minutes_by_day} - id: {id(jogging_minutes_by_day)}")
print(f"jogging_minutes_by_day[1]: {jogging_minutes_by_day[1]} - id: {id(jogging_minutes_by_day)}")

jogging_minutes_by_day[1] = {'Tuesday', 55}
print(f"jogging_minutes_by_day: {jogging_minutes_by_day} - id: {id(jogging_minutes_by_day)}")

jogging_minutes_by_day[0] = 'Have a rest'
print(f"jogging_minutes_by_day: {jogging_minutes_by_day} - id: {id(jogging_minutes_by_day)}")

c = 110
print(f"jogging_minutes_by_day: {jogging_minutes_by_day} - id: {id(jogging_minutes_by_day)}")

new_jogging_minutes_by_day = jogging_minutes_by_day
d = 25
print(f"jogging_minutes_by_day: {jogging_minutes_by_day} - id: {id(jogging_minutes_by_day)}")
print(f"new_jogging_minutes_by_day: {new_jogging_minutes_by_day} - id: {id(jogging_minutes_by_day)}")

jogging_minutes_by_day[0] = 'Zzzzzz...'
print(f"jogging_minutes_by_day: {jogging_minutes_by_day} - id: {id(jogging_minutes_by_day)}")
print(f"new_jogging_minutes_by_day: {new_jogging_minutes_by_day} - id: {id(jogging_minutes_by_day)}")

print("-----------------")

# Playing with dict variables
print(f"sports: {sports} - id: {id(sports)}")

# sports[0] = 'football'  # tuples do not support item assigment
# print(f"sports: {sports}")

sports_copy = sports
print(f"sports: {sports} - id: {id(sports)}")
print(f"sports_copy: {sports_copy} - id: {id(sports_copy)}")

sports_copy = ()
print(f"sports: {sports} - id: {id(sports)}")
print(f"sports_copy: {sports_copy} - id: {id(sports_copy)}")

