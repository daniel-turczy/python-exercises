"""
Python has a removesuffix() method that works exactly like removeprefix().
Assign the value 'python_notes.txt' to a variable called filename. Then use the
removesuffix() method to display the filename without the file extension,
like some browsers do.
"""

filename = 'python_notes.txt'

print(filename)
print(filename.removesuffix(".txt"))
print(filename.removeprefix("python_"))
