# not necessary, can be avoided with loops and if-statement but are more concise

# The classes a student is registered for
classes_registered = ['ITEC 1150', 'ITEC 1100', 'ENGL 1340', 'MATH 1100']

# Make a list of only the ITEC classes
only_itec = [c for c in classes_registered if c.startswith('ITEC')]
print(only_itec)


# Record temperatures ever day. Record -1 if not possible to take measurement.
high_temps = [-1, 78, 72, 67, -1, 51, 87, 82, -1, 54, 67, 78, -1, 70]

# make each number in the list +1 higher
numbers = [2, 4, 6]

plus_one_numbers = [plus_one + 1 for plus_one in numbers]
print(plus_one_numbers)

numbers = [0, 2, 4, 0, 22, 1]

# removes all zeros from the list of numbers
no_zeros = [not_zero for not_zero in numbers if not_zero != 0]
print(no_zeros)

numbers_list = [0, 10, 4, 0, 32]
non_zeros_doubled = [n*2 for n in numbers_list if n != 0]
print(non_zeros_doubled)