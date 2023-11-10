"""
Lesson 1 - Functional Programming
"""


# higher-order functions
def upper_func(func, arg):
    return func(func(arg))


def lower_func(arg):
    return (arg * 2 + 3) / 2.5


print(upper_func(lower_func, 10))


# pure and impure functions

# pure function
def pure_func(x, y):
    temp = x + 2 * y
    return temp / (x * 2) + y


print(pure_func(5, 6))

# Impure function
z = 12


def impure_func(x, y):
    temp = x + (2 * y) + (z * 3)
    return temp / (x * 2) + y


print(impure_func(5, 6))

"""
Using pure functions has both advantages and disadvantages.
Pure functions are:

- easier to reason about and test.
- easier to run in parallel.
- more efficient. Once the function has been evaluated for an input, the result can be stored and referred to the 
next time the function of that input is needed, reducing the number of times the function is called. This is called 
memoization.


-Pure functions are more difficult to write in some situations.
"""

"""
Lesson 2 - Lambdas
"""


def polynomial(x):
    return x ** 2 + 5 * x + 4


print('')
print(polynomial(5))

# Lambdas
print((lambda x: x ** 2 + 5 * x + 4)(-4))

"""
Lesson 3 - Map & Filter
"""

# map
print('\nmap')

list_of_numbers = [11, 22, 33, 44, 55, 66, 77]
print(list_of_numbers)

print(list(map(lambda x: x ** 2 - 6, list_of_numbers)))

# filter
print('\nfilter')

list_of_numbers1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list_of_numbers1)

print(list(filter(lambda x: x % 2 == 0, list_of_numbers1)))

"""
Generators
"""


def generator():
    i = 5
    while i > 0:
        yield i
        i -= 1


for i in generator():
    print(i)

"""
The yield statement is used to define a generator, replacing the return of a function to provide a result to its 
caller without destroying local variables.

Due to the fact that they yield one item at a time, generators don't have the memory restrictions of lists. 
In fact, they can be infinite!
"""


def even_num_func(x):
    for num in range(x):
        if num % 2 == 0:
            yield num


print(list(even_num_func(25)))