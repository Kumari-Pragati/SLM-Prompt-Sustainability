import unittest
from mbpp_471_code import find_remainder

class TestFindRemainder(unittest.TestCase):

    def test_find_remainder_empty_list(self):
        self.assertEqual(find_remainder([], len([]), 3), 1)

    def test_find_remainder_single_element(self):
        self.assertEqual(find_remainder([1], 1, 3), 1)

    def test_find_remainder_multiple_elements(self):
        self.assertEqual(find_remainder([1, 2, 3], 3, 5), 24)

    def test_find_remainder_negative_numbers(self):
        self.assertEqual(find_remainder([-1, -2, -3], 3, 5), 24)

    def test_find_remainder_zero(self):
        self.assertEqual(find_remainder([0], 1, 3), 1)

    def test_find_remainder_large_numbers(self):
        self.assertEqual(find_remainder([1000000001, 1000000002, 1000000003], 3, 5), 24)
