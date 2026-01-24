import unittest
from mbpp_769_code import Diff

class TestDiff(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(Diff([1, 2, 3], [2, 3, 4]), [[1], [4]])

    def test_empty_lists(self):
        self.assertEqual(Diff([], []), [])

    def test_one_empty_list(self):
        self.assertEqual(Diff([1, 2, 3], []), [[1, 2, 3]])

    def test_duplicate_elements(self):
        self.assertEqual(Diff([1, 2, 2, 3], [2, 2, 3, 4]), [[1], [4]])

    def test_same_elements(self):
        self.assertEqual(Diff([1, 2, 3], [1, 2, 3]), [])

    def test_negative_numbers(self):
        self.assertEqual(Diff([-1, -2, -3], [-2, -3, -4]), [[-1], [-4]])

    def test_large_numbers(self):
        self.assertEqual(Diff([1000, 2000, 3000], [2000, 3000, 4000]), [[1000], [4000]])

    def test_non_integer_elements(self):
        self.assertEqual(Diff([1.1, 2.2, 3.3], [2.2, 3.3, 4.4]), [[1.1], [4.4]])

    def test_string_elements(self):
        self.assertEqual(Diff(['a', 'b', 'c'], ['b', 'c', 'd']), [['a'], ['d']])
