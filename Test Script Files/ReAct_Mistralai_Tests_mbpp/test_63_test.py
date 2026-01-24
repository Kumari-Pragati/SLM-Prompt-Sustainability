import unittest
from mbpp_63_code import max_difference

class TestMaxDifference(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(max_difference([]), 0)

    def test_single_element_list(self):
        self.assertEqual(max_difference([1]), 0)

    def test_two_elements_list(self):
        self.assertEqual(max_difference([1, 2]), 1)

    def test_positive_numbers_list(self):
        self.assertEqual(max_difference([1, 2, 3, 4, 5]), 4)

    def test_negative_numbers_list(self):
        self.assertEqual(max_difference([-1, -2, -3, -4, -5]), 6)

    def test_mixed_numbers_list(self):
        self.assertEqual(max_difference([1, -2, 3, -4, 5]), 7)

    def test_large_numbers_list(self):
        self.assertEqual(max_difference([1000000001, 1000000000, 1000000002]), 3)

    def test_negative_large_numbers_list(self):
        self.assertEqual(max_difference([-1000000001, -1000000000, -1000000002]), 3)

    def test_list_with_zero(self):
        self.assertEqual(max_difference([0, 1, 2, 3, 4]), 4)

    def test_list_with_duplicates(self):
        self.assertEqual(max_difference([1, 1, 2, 3, 4]), 3)

    def test_list_with_only_zeros(self):
        self.assertEqual(max_difference([0, 0, 0]), 0)

    def test_list_with_negative_zeros(self):
        self.assertEqual(max_difference([-0, 0, 0]), 0)

    def test_list_with_floats(self):
        self.assertEqual(max_difference([1.1, 2.2, 3.3]), 1.9)

    def test_list_with_negative_floats(self):
        self.assertEqual(max_difference([-1.1, -2.2, -3.3]), 3.4)

    def test_list_with_mixed_floats(self):
        self.assertEqual(max_difference([1.1, -2.2, 3.3]), 3.4)
