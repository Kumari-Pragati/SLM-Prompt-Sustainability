import unittest
from mbpp_697_code import count_even

class TestCountEven(unittest.TestCase):

    def test_count_even(self):
        self.assertEqual(count_even([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 5)
        self.assertEqual(count_even([1, 3, 5, 7, 9]), 0)
        self.assertEqual(count_even([2, 4, 6, 8, 10]), 5)
        self.assertEqual(count_even([2, 4, 6, 8, 10, 12, 14, 16, 18, 20]), 10)
        self.assertEqual(count_even([]), 0)
        self.assertEqual(count_even([1]), 0)
        self.assertEqual(count_even([2]), 1)
        self.assertEqual(count_even([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]), 10)
