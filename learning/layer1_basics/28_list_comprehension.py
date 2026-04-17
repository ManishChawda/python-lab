#1st 
numbers = [1, 2, 3, 4, 5]
squared = [x * x for x in numbers]
print(squared)

#2nd
numbers = [1, 2, 3, 4, 5]
squared = []
for x in numbers:
    squared.append(x * x)

print("Squares:", squared)

#3rd
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)

#4th
numbers = [1, 2, 3, 4, 5, 6]
for x in numbers:
    if x % 2 == 0:
        print("Even:", x)

#5th    
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = []
for x in numbers:
    if x % 2 == 0:
        even_numbers.append(x)

print(even_numbers)