import os

with open('Day1/advent_1.txt', 'r') as floor_file:
    floor_code = floor_file.read()

floor_now = 0
for char in floor_code:
    print(char)
    if char == '(':
        floor_now += 1
    elif char == ')':
        floor_now -= 1
    else:
        print(f"Char {char} unknown")
    print(f"Floor now {floor_now}")
