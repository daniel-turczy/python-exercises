"""
Ordinal numbers indicate their position in a list, such as 1st or 2nd.

- Store the numbers 1 to 9 in a list.
- Loop through the list.
- Use and if-elif-else chain inside the loop to print the proper ordinal ending
  for each number. Your output should read "1st 2nd 3rd" etc., and each result
  should be on a separate line.
"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for num in numbers:
    if num == 1:
        suffix = "st"
    elif num == 2:
        suffix = "nd"
    elif num == 3:
        suffix = "rd"
    else:
        suffix = "th"
    
    print(f"{num}{suffix}")