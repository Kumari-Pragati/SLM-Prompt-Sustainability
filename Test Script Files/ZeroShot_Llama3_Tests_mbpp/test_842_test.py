import unittest
from mbpp_842_code import get_odd_occurence

class TestGetOddOccurrence(unittest.TestCase):

    def test_get_odd_occurrence(self):
        self.assertEqual(get_odd_occurence([1, 2, 3, 2, 3, 1], 6), 1)
        self.assertEqual(get_odd_occurence([5, 5, 5, 5, 5, 5], 6), 5)
        self.assertEqual(get_odd_occurrence([1, 2, 3, 4, 5, 6], 6), -1)
        self.assertEqual(get_odd_occurrence([1, 1, 1, 1, 1, 1], 6), 1)
        self.assertEqual(get_odd_occurrence([1, 2, 3, 4, 5, 6, 7], 7), 7)
        self.assertEqual(get_odd_occurrence([1, 1, 1, 1, 1, 1, 1], 7), 1)
        self.assertEqual(get_odd_occurrence([1, 2, 3, 4, 5, 6, 7, 8], 8), -1)
