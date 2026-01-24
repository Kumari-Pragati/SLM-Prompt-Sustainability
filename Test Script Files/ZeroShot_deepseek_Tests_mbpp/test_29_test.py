import unittest
from mbpp_29_code import get_Odd_Occurrence

class TestGetOddOccurrence(unittest.TestCase):

    def test_get_Odd_Occurrence(self):
        self.assertEqual(get_Odd_Occurrence([2, 3, 5, 4, 5, 2, 4, 3, 5, 2, 4, 4, 2], 13), 5)
        self.assertEqual(get_Odd_Occurrence([1, 1, 2, 2, 1, 1, 2, 2, 13, 13, 13], 11), 13)
        self.assertEqual(get_Odd_Occurrence([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10), -1)
        self.assertEqual(get_Odd_Occurrence([1, 1, 1, 1, 1, 1, 10, 10, 10, 10], 10), 1)
        self.assertEqual(get_Odd_Occurrence([10, 20, 30, 40, 50, 60, 70, 80, 90, 100], 10), -1)
