import unittest
from mbpp_68_code import is_Monotonic

class TestIsMonotonic(unittest.TestCase):

    def test_typical_case_increasing(self):
        self.assertTrue(is_Monotonic([1, 2, 3, 4, 5]))

    def test_typical_case_decreasing(self):
        self.assertTrue(is_Monotonic([5, 4, 3, 2, 1]))

    def test_typical_case_constant(self):
        self.assertTrue(is_Monotonic([1, 1, 1, 1, 1]))

    def test_edge_case_single_element(self):
        self.assertTrue(is_Monotonic([1]))

    def test_edge_case_empty_list(self):
        self.assertTrue(is_Monotonic([]))

    def test_edge_case_increasing_with_duplicates(self):
        self.assertTrue(is_Monotonic([1, 2, 2, 3, 4]))

    def test_edge_case_decreasing_with_duplicates(self):
        self.assertTrue(is_Monotonic([4, 3, 2, 2, 1]))

    def test_invalid_input_non_integer(self):
        with self.assertRaises(TypeError):
            is_Monotonic([1, 'a', 2])

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            is_Monotonic('1,2,3')
