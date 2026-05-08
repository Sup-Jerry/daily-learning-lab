numbers = [3, 7, 2, 9, 5]

print("Original numbers:", numbers)

sorted_numbers = sorted(numbers)
even_numbers = [number for number in numbers if number % 2 == 0]
total = sum(numbers)

print("Sorted numbers:", sorted_numbers)
print("Even numbers:", even_numbers)
print("Total:", total)

largest = max(numbers)
smallest = min(numbers)
print("Largest:", largest)
print("Smallest:", smallest)
