"""
Make a list of numbers from one to one million, and then use min() and max()
to make sure your list actaully starts at one and ends at one million. Also,
use the sum() functions to see how quickly Python can add one million numbers.
"""

numbers = [num for num in range(1,1000001)]

print(f"Smallest number: {min(numbers)}")
print(f"Biggest number: {max(numbers)}")
print(f"Sum of numbers: {sum(numbers)}")