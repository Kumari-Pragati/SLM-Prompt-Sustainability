import unittest
from mbpp_258_code import count_odd

class TestCountOdd(unittest.TestCase):

    def test_count_odd(self):
        self.assertEqual(count_odd([1, 2, 3, 4, 5]), 3)
        self.assertEqual(count_odd([2, 4, 6, 8, 10]), 0)
        self.assertEqual(count_odd([1, 3, 5, 7, 9]), 5)
        self.assertEqual(count_odd([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 5)
        self.assertEqual(count_odd([]), 0)
        self.assertEqual(count_odd([1]), 1)
        self.assertEqual(count_odd([2]), 0)
        self.assertEqual(count_odd([1, 2]), 1)
        self.assertEqual(count_odd([2, 2]), 0)
        self.assertEqual(count_odd([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]), 8)
