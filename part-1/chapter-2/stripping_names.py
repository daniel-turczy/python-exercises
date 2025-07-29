"""
Use a variable to represent a person's name, and include some whitespace
characters at the beginning and end of the name. Make sure you use each
character combination, "\t" and "\n", at least once. Then print the name using
each of the three stripping functions, lstrip(), rstrip(), and strip().
"""

name = "\n   Christian  \t\t   "
print("Before:")
print(name)

print("\nAfter:")
print(name.lstrip()) #strips whitespace to left of string
print(name.rstrip()) #strips right
print(name.strip()) #strips both sides