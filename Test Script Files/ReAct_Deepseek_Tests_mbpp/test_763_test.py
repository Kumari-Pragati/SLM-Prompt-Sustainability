import unittest
from mbpp_763_code import find_Min_Diff

class TestFindMinDiff(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_Min_Diff([1, 5, 3, 19, 18, 25], 6), 1)

    def test_single_element(self):
        self.assertEqual(find_Min_Diff([5], 1), 0)

    def test_sorted_array(self):
        self.assertEqual(find_Min_Diff([1, 2, 3, 4, 5], 5), 1)

    def test_reverse_sorted_array(self):
        self.assertEqual(find_Min_Diff([5, 4, 3, 2, 1], 5), 1)

    def test_duplicate_elements(self):
        self.assertEqual(find_Min_Diff([1, 1, 1, 1, 1], 5), 0)

    def test_large_numbers(self):
        self.assertEqual(find_Min_Diff([10**6, 2*10**6, 3*10**6], 3), 10**6)

    def test_negative_numbers(self):
        self.assertEqual(find_Min_Diff([-5, -3, -1, 0, 1, 3], 6), 1)

    def test_empty_array(self):
        with self.assertRaises(ValueError):
            find_Min_Diff([], 0)
