"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Square.

The Sieve of Eratosthenes is an algorithm used to generate all prime numbers smaller than N. The method is to take increasingly larger prime numbers, and mark their multiples as composite.

For example, to find all primes less than 100, we would first mark [4, 6, 8, ...] (multiples of two), then [6, 9, 12, ...] (multiples of three), and so on. Once we have done this for all primes less than N, the unmarked numbers that remain will be prime.

Implement this algorithm.

Bonus: Create a generator that produces primes indefinitely (that is, without taking N as an input).
"""
import unittest

def primes(num):
    primelist = []
    for i in range(2, num+1):
        primelist.append(i)
        for j in range(2, i):
            if i%j == 0:
                primelist.pop()
                break
    return primelist

class Test(unittest.TestCase):
    def setUp(self):
        self.input = 20
        self.expected = [2,3,5,7,11,13,17,19]

    def test_equality(self):
        self.assertListEqual(primes(self.input), self.expected)

if __name__ == "__main__":
    print(primes(1000))
    unittest.main()
