import unittest
from mbpp_807_code import first_odd

class TestFirstOdd(unittest.TestCase):

    def test_first_odd(self):
        self.assertEqual(first_odd([1, 2, 3, 4, 5]), 1)
        self.assertEqual(first_odd([2, 4, 6, 8, 10]), -1)
        self.assertEqual(first_odd([1, 3, 5, 7, 9]), 1)
        self.assertEqual(first_odd([2, 4, 6, 8, 10, 12]), -1)
        self.assertEqual(first_odd([1, 2, 3, 4, 5, 6]), 1)
        self.assertEqual(first_odd([2, 4, 6, 8, 10, 12, 14]), -1)
        self.assertEqual(first_odd([1, 3, 5, 7, 9, 11, 13]), 1)
        self.assertEqual(first_odd([2, 4, 6, 8, 10, 12, 14, 16]), -1)
        self.assertEqual(first_odd([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]), 1)
        self.assertEqual(first_odd([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]), -1)
