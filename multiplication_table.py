#!/usr/bin/env python3
'''Prints out a multiplacation table'''
# Get the no. of rows and cols in the table from user
try:
    size = int(input('Enter Multiplication Table size: '))
except ValueError:
    print('Oops!.... Expected Integer')

# Print a size x size multiplcation table

# Headers  
print('     ', end='') # Blank top-leftmost cell
for column in range(1, size + 1):
    print('{0:4}'.format(column), end='') # Column Header Number
print() # Move down to the next line
# col-header and rows sepaartor
print('    +', end='')
for column in range(1, size + 1):
    print('----', end='') # Separator line
print() # Move down to next line

# Rows and table content
for row in range(1, size + 1):
    print('{0:3} |'.format(row), end='')
    for column in range(1, size + 1):
        product = row * column # Compute product
        print('{0:4}'.format(product), end='')
    print() # Move cursor to the next row