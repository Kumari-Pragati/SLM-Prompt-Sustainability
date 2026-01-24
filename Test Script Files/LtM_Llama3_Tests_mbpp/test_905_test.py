import unittest
from mbpp_905_code import sum_of_square

class TestSumOfSquare(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(sum_of_square(0), 0)
        self.assertEqual(sum_of_square(1), 1)
        self.assertEqual(sum_of_square(2), 5)
        self.assertEqual(sum_of_square(3), 14)
        self.assertEqual(sum_of_square(4), 30)

    def test_edge(self):
        self.assertEqual(sum_of_square(-1), 0)
        self.assertEqual(sum_of_square(0), 0)
        self.assertEqual(sum_of_square(1), 1)
        self.assertEqual(sum_of_square(2), 5)
        self.assertEqual(sum_of_square(3), 14)

    def test_complex(self):
        self.assertEqual(sum_of_square(5), 55)
        self.assertEqual(sum_of_square(10), 385)
        self.assertEqual(sum_of_square(20), 4410)
