# Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.


def solution(number):
    sum_multiplies = 0
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            sum_multiplies += i
    return sum_multiplies


# refactored!:
#
# def solution(num):
#    return sum(i for i in range(num) if i % 3 == 0 or i % 5 == 0)


# reminded Fizz-Buzz task ))
# Write a program that prints number but
# for multiples of three print “Fizz” instead of the number
# and for the multiples of five print “Buzz”.
# For numbers which are multiples of both three and five print “FizzBuzz”.


def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return "FizzBuzz"
    if input % 3 == 0:
        return "Fizz"
    if input % 5 == 0:
        return "Buzz"
    return input
