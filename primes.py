"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if number_of_primes <=0:
        raise ValueError('Number is 0 or negative.')
    list = []
    i = 2
    while len(list) < number_of_primes:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            list.append(i)
        i +=1
    return list

