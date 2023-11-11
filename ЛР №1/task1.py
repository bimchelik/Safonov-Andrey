numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

missing_number = numbers.index(None)
numbers[missing_number] = 0

total = sum(numbers)
count = len(numbers)
average = total / count
numbers[missing_number] = average

print("Измененный список:", numbers)