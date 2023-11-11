"""
Write a function that calculates the new price of an item after the discount using lambda function

Sample Input
50
10

Sample Output
45.0
"""
price = int(input('Enter the price of the item: '))
discount_percentage = int(input('Enter the discount percentage: '))

new_price = (lambda a, b: a - (a * b / 100))(price, discount_percentage)

print('The item price after the discount is: ', new_price)

"""
You work on a payroll program.
Given a list of salaries, you need to take the bonus (in percent) everybody is getting as input
and increase all the salaries by that amount. Output the resulting list.
"""

salaries = [2000, 1800, 3100, 4400, 1500]
bonus = int(input('Enter the bonus percentage: '))

salary_cal = list(map(lambda x: int(x + (x * bonus / 100)), salaries))

print(salary_cal)

"""
Finding prime numbers is a common coding interview task.
The given code defines a function isPrime(x), which returns True if x is prime.
You need to create a generator function primeGenerator(), that will take two numbers as arguments, and use the
isPrime() function to output the prime numbers in the given range (between the two arguments).

Sample Input
10
20

Sample Output
[11, 13, 17, 19]
"""


# prime number: [1, 2, 3, 5, 7, 11 ...]


def isPrime(x):
    if x < 2:
        return False
    elif x == 2:
        return True
    for num in range(2, x):
        if x % num == 0:
            return False
    return True


def primeGenerator(num1, num2):
    for i in range(num1, num2):
        if isPrime(i):
            yield i


print('\nWrite a code to output the prime numbers in the given range (between the two arguments). ')
input1 = int(input('Enter the first number: '))
input2 = int(input('Enter the second number: '))

print(list(primeGenerator(input1, input2)))

"""
You are working on an invoicing system.
The system has an already defined invoice() function, which takes the invoice number as argument and outputs it.
You need to add a decorator for the invoice() function, that will print the invoice in the following format:

Sample Input
42

Sample Output
*********
INVOICE #42
*********
END OF PAGE
"""


def decor(func):
    def invoice_temp(num):
        print('*********')
        func(num)
        print('*********')
        print("END OF PAGE")

    return invoice_temp


@decor
def invoice(num):
    print('INVOICE #', num)


invoice(input('\nEnter Your invoice Number: '))
