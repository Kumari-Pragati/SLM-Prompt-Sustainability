import unittest
from mbpp_105_code import count

class TestCountFunction(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(count([]), 0)

    def test_single_element_list(self):
        self.assertEqual(count([1]), 1)

    def test_multiple_elements_list(self):
        self.assertEqual(count([1, 2, 3]), 6)

    def test_negative_numbers(self):
        self.assertEqual(count([-1, -2, -3]), -6)

    def test_mixed_positive_and_negative_numbers(self):
        self.assertEqual(count([1, -2, 3, -4]), 0)

    def test_list_with_duplicates(self):
        self.assertEqual(count([1, 1, 2, 2, 3]), 6)

    def test_list_with_zero(self):
        self.assertEqual(count([0, 1, 2]), 3)
