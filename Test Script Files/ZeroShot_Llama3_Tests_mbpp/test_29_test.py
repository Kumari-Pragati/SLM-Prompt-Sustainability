import unittest
from mbpp_29_code import get_Odd_Occurrence

class TestGetOddOccurrence(unittest.TestCase):

    def test_get_Odd_Occurrence(self):
        self.assertEqual(get_Odd_Occurrence([1, 2, 3, 4, 5], 5), 1)
        self.assertEqual(get_Odd_Occurrence([1, 2, 2, 3, 4, 5], 6), 1)
        self.assertEqual(get_Odd_Occurrence([1, 1, 1, 1, 1, 1], 6), 1)
        self.assertEqual(get_Odd_Occurrence([1, 2, 3, 4, 5, 6], 6), -1)
        self.assertEqual(get_Odd_Occurrence([1, 1, 2, 2, 3, 3], 6), 1)
        self.assertEqual(get_Odd_Occurrence([1, 2, 3, 4, 5, 5], 6), 5)
        self.assertEqual(get_Odd_Occurrence([1, 2, 3, 4, 5, 6, 7], 7), 1)
        self.assertEqual(get_Odd_Occurrence([1, 1, 1, 1, 1, 1, 1], 7), 1)
        self.assertEqual(get_Odd_Occurrence([1, 2, 3, 4, 5, 6, 7, 8], 8), -1)
