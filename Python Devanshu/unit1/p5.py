'''Write a program to create and manipulate lists
using indexing slicing and list comprehensions.'''

numbers = [10, 20, 30, 40, 50, 60]

print("Original List:", numbers)

print("First element:", numbers[0])
print("Last element:", numbers[-1])

print("First three elements:", numbers[:3])
print("Last three elements:", numbers[3:])
print("Elements from index 1 to 4:", numbers[1:5])


numbers[2] = 35
print("After modifying third element:", numbers)


numbers.append(70)
print("After appending 70:", numbers)

numbers.remove(40)
print("After removing 40:", numbers)


squares = [x**2 for x in numbers]
print("Squares of elements:", squares)


even_numbers = [x for x in numbers if x % 2 == 0]
print("Even numbers:", even_numbers)
