import unittest
from mbpp_68_code import is_Monotonic

class TestIsMonotonic(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(is_Monotonic([1, 2, 3, 4, 5]))

    def test_decreasing(self):
        self.assertTrue(is_Monotonic([5, 4, 3, 2, 1]))

    def test_increasing(self):
        self.assertTrue(is_Monotonic([1, 2, 3, 4, 5]))

    def test_constant(self):
        self.assertTrue(is_Monotonic([1, 1, 1, 1, 1]))

    def test_edge_case(self):
        self.assertTrue(is_Monotonic([1, 1]))

    def test_empty_list(self):
        with self.assertRaises(IndexError):
            is_Monotonic([])

    def test_single_element_list(self):
        self.assertTrue(is_Monotonic([1]))

    def test_list_with_duplicates(self):
        self.assertTrue(is_Monotonic([1, 2, 2, 3, 3, 4, 5]))

    def test_list_with_duplicates_increasing(self):
        self.assertTrue(is_Monotonic([1, 2, 2, 3, 3, 4, 5]))

    def test_list_with_duplicates_decreasing(self):
        self.assertTrue(is_Monotonic([5, 4, 4, 3, 3, 2, 1]))
