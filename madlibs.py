# string concatenation
# Game 1:
variable1 = "some string"

print("this variable is " + variable1)
print("this variable is {}".format(variable1))
print(f"this vatiable is {variable1}")

# we want to create a string that says 
# "Hello, my name is _______"

# Game 2:
adjective1 = input("Adjective: ")
adjective2 = input("Adjective: ")
verb1 = input("Verb: ")
famous_person = input("Famous person: ")

madlib = f"Coding is so {adjective1}! It makes me so {adjective2} because I love to {verb1}. Stay consistent like {famous_person}."

print(madlib)