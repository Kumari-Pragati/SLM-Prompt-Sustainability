import unittest
from mbpp_824_code import remove_even

class TestRemoveEven(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(remove_even([]), [])

    def test_single_element_list(self):
        self.assertEqual(remove_even([1]), [1])

    def test_even_element_list(self):
        self.assertEqual(remove_even([2, 4, 6]), [])

    def test_mixed_list(self):
        self.assertEqual(remove_even([1, 2, 3, 4, 5]), [1, 3, 5])

    def test_list_with_duplicates(self):
        self.assertEqual(remove_even([2, 4, 2, 6, 4]), [])

    def test_list_with_negative_numbers(self):
        self.assertEqual(remove_even([-2, -4, 1, 3]), [-2, -4])

    def test_list_with_zero(self):
        self.assertEqual(remove_even([0, 1, 2]), [1])

    def test_list_with_max_value(self):
        self.assertEqual(remove_even([100, 101, 102]), [101, 102])
