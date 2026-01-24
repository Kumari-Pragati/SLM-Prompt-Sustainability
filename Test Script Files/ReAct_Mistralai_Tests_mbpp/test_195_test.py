import unittest
from mbpp_195_code import first

class TestFirstFunction(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(first([], 5, 0), -1)

    def test_single_element(self):
        self.assertEqual(first([5], 5, 0), 0)
        self.assertEqual(first([5], 4, 0), -1)

    def test_multiple_elements_found(self):
        self.assertEqual(first([1, 2, 3, 4, 5], 4, 0), 3)
        self.assertEqual(first([1, 2, 3, 4, 5], 5, 0), 4)

    def test_multiple_elements_not_found(self):
        self.assertEqual(first([1, 2, 3, 4, 5], 6, 0), -1)

    def test_elements_out_of_range(self):
        self.assertEqual(first([1, 2, 3, 4, 5], 5, 5), -1)
        self.assertEqual(first([1, 2, 3, 4, 5], 5, -1), -1)

    def test_negative_numbers(self):
        self.assertEqual(first([-1, -2, -3, -4, -5], -4, 0), 3)
        self.assertEqual(first([-1, -2, -3, -4, -5], -5, 0), 4)
