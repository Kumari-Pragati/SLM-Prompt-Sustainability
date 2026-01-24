import unittest
from mbpp_769_code import Diff

class TestDiff(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(Diff([1, 2, 3], [2, 3, 4]), [[1], [4]])

    def test_empty_lists(self):
        self.assertEqual(Diff([], []), [])

    def test_same_elements(self):
        self.assertEqual(Diff([1, 2, 3], [1, 2, 3]), [])

    def test_one_empty_list(self):
        self.assertEqual(Diff([1, 2, 3], []), [[1, 2, 3]])

    def test_duplicate_elements(self):
        self.assertEqual(Diff([1, 2, 2, 3], [2, 2, 3, 4]), [[1], [4]])

    def test_negative_numbers(self):
        self.assertEqual(Diff([-1, -2, -3], [-2, -3, -4]), [[-1], [-4]])

    def test_mixed_types(self):
        self.assertEqual(Diff([1, '2', 3], [2, '2', 4]), [[1], [4]])

    def test_non_integer_elements(self):
        self.assertEqual(Diff(['1', '2', '3'], ['2', '3', '4']), [['1'], ['4']])
