# coding = utf-8
# Author: Celine
# Date: 2023/4/5 23:01

def prime_checker(number):
    '''Solution1.0: divided by 2, 3, 5, 7'''
    # if number % 2 != 0 and number % 3 != 0 and number % 5 != 0 and number % 7 != 0:
    #     print("It's a prime number.")
    # else:
    #     print("It's not a prime number.")

    ''' Solution1.1: 6x + 1 or 6x + 5 '''
    # if number == 0 or number == 1:
    #     print("It's not a prime number.")

    # if number % 6 == 1 or number % 6 == 5:
    #     print("It's a prime number.")
    # else:
    #     print("It's not a prime number.")

    ''' Solution2.0: every number divide by the number less than it '''
    # if number == 2 or number == 3:
    #     print("It's a prime number.")
    #
    # prime_counter = 0
    # for divisor in range(2, number):
    #     if number % divisor == 0:
    #         print("It's not a prime number.")
    #         break
    #     else:
    #         prime_counter += 1
    #
    # if prime_counter == (number - 2):
    #     print("It's a prime number.")

    ''' Solution2.1: Using for loop + flag '''
    is_prime = True
    for divisor in range(2, number):
        if number % divisor == 0:
            is_prime = False

    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")


n = int(input("Check this number: "))
prime_checker(number=n)