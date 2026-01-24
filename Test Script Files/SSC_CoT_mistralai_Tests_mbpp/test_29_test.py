import unittest
from mbpp_29_code import get_Odd_Occurrence

class TestGetOddOccurrence(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(get_Odd_Occurrence([1, 2, 3, 2, 2, 4, 2, 5], 8), 1)
        self.assertEqual(get_Odd_Occurrence([4, 4, 4, 4, 4, 4, 4, 5], 8), 5)
        self.assertEqual(get_Odd_Occurrence([1, 1, 1, 1, 1, 1, 1, 2], 8), -1)

    def test_edge_cases(self):
        self.assertEqual(get_Odd_Occurrence([1], 1), 1)
        self.assertEqual(get_Odd_Occurrence([1, 1], 2), -1)
        self.assertEqual(get_Odd_Occurrence([1, 1, 1], 3), 1)
        self.assertEqual(get_Odd_Occurrence([1, 1, 1, 1], 4), -1)

    def test_empty_list(self):
        self.assertEqual(get_Odd_Occurrence([], 0), -1)

    def test_invalid_input(self):
        self.assertRaises(TypeError, get_Odd_Occurrence, [1, 2, 3], 'invalid size')
        self.assertRaises(TypeError, get_Odd_Occurrence, [1, 2, 3], 3.14)
