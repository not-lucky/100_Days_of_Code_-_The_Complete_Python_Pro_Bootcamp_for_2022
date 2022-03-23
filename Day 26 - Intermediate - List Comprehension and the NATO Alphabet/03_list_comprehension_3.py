'''
Instructions

Take a look inside file1.txt and file2.txt. They each contain a bunch of
 numbers, each number on a new line.

You are going to create a list called result which contains the numbers that
 are common in both files.

e.g. if file1.txt contained:

1
2
3

and file2.txt contained:

2
3
4

result = [2, 3]

IMPORTANT: The result should be a list that contains Integers, not Strings.
Try to use List Comprehension instead of a Loop.
Example Output

[3, 6, 5, 33, 12, 7, 42, 13]
'''

with open('file1.txt') as f1:
    f1_list = f1.read().splitlines()

with open('file2.txt') as f2:
    f2_list = f2.read().splitlines()

result = [int(num) for num in f1_list if num in f2_list]


# Write your code above 👆

print(result)
