#!/usr/bin/env python3
'''Prints out a multiplacation table'''
# Get the no. of rows and cols in the table from user
try:
    size = int(input('Enter Multiplication Table size: '))
except ValueError:
    print('Oops!.... Expected Integer')

# Print a size x size multiplcation table
for row in range(1, size + 1):
    for column in range(1, size + 1):
        product = row * column # Compute product
        print(product, end=' ')
    print() # Move cursor to the next row