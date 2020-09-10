import unittest
from katas import *


class TestKatas(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)

    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-1, 1), -1)
        self.assertEqual(multiply(-1, -1), 1)

    def test_power(self):
        self.assertEqual(power(2, 2), 4)
        self.assertEqual(power(10, 4), 10000)
        self.assertEqual(power(6, 8), 1679616)

    def test_factorial(self):
        self.assertEqual(factorial(4), 24)
        self.assertEqual(factorial(7), 5040)
        self.assertEqual(factorial(5), 120)

    def test_fibonacci(self):
        self.assertEqual(fibonacci(6), 5)
        self.assertEqual(fibonacci(8), 13)
        self.assertEqual(fibonacci(10), 34)


if __name__ == '__main__':
    unittest.main()
