import unittest
from mbpp_29_code import get_Odd_Occurrence

class TestGetOddOccurrence(unittest.TestCase):

    def test_simple_occurrence(self):
        self.assertEqual(get_Odd_Occurrence([1, 2, 3, 2, 2, 3, 1], 7), 1)
        self.assertEqual(get_Odd_Occurrence([4, 4, 4, 4, 4, 4, 4, 5], 8), 5)

    def test_edge_cases(self):
        self.assertEqual(get_Odd_Occurrence([], 0), -1)
        self.assertEqual(get_Odd_Occurrence([1], 1), -1)
        self.assertEqual(get_Odd_Occurrence([1, 1], 2), -1)
        self.assertEqual(get_Odd_Occurrence([1, 2, 1], 3), 1)
        self.assertEqual(get_Odd_Occurrence([1, 1, 1], 3), -1)

    def test_complex_cases(self):
        self.assertEqual(get_Odd_Occurrence([1, 2, 3, 2, 3, 2, 1, 3, 2], 9), 1)
        self.assertEqual(get_Odd_Occurrence([1, 1, 2, 2, 3, 3, 2, 2, 1], 9), -1)
