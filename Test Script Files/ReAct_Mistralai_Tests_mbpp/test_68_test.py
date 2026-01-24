import unittest
from mbpp_68_code import is_Monotonic

class TestIsMonotonic(unittest.TestCase):

    def test_monotonic_increasing(self):
        self.assertTrue(is_Monotonic([1, 2, 3, 4, 5]))

    def test_monotonic_decreasing(self):
        self.assertTrue(is_Monotonic([5, 4, 3, 2, 1]))

    def test_monotonic_mixed(self):
        self.assertTrue(is_Monotonic([1, 3, 5, 2, 4]))

    def test_single_element(self):
        self.assertTrue(is_Monotonic([1]))

    def test_empty_list(self):
        self.assertTrue(is_Monotonic([]))

    def test_duplicate_elements(self):
        self.assertTrue(is_Monotonic([1, 1, 2, 3]))

    def test_edge_case_first_decreasing(self):
        self.assertTrue(is_Monotonic([5, 4, 3, 2, 1, 0]))

    def test_edge_case_last_increasing(self):
        self.assertTrue(is_Monotonic([0, 1, 2, 3, 4, 5]))

    def test_edge_case_last_decreasing(self):
        self.assertTrue(is_Monotonic([5, 4, 3, 2, 1, 0, -1]))

    def test_error_case_non_iterable(self):
        with self.assertRaises(TypeError):
            is_Monotonic('abc')
