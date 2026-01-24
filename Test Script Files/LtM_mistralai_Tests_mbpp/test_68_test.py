import unittest
from mbpp_68_code import is_Monotonic

class TestIsMonotonic(unittest.TestCase):

    def test_simple_increasing(self):
        self.assertTrue(is_Monotonic([1, 2, 3, 4, 5]))

    def test_simple_decreasing(self):
        self.assertTrue(is_Monotonic([5, 4, 3, 2, 1]))

    def test_empty_list(self):
        self.assertTrue(is_Monotonic([]))

    def test_single_element(self):
        self.assertTrue(is_Monotonic([1]))

    def test_duplicate_elements(self):
        self.assertTrue(is_Monotonic([1, 1, 2, 2, 3]))

    def test_edge_case_increasing(self):
        self.assertTrue(is_Monotonic([0, 1, 2, 3, 4]))

    def test_edge_case_decreasing(self.test_edge_case_increasing):
        self.assertTrue(is_Monotonic([4, 3, 2, 1, 0]))

    def test_mixed_case(self):
        self.assertTrue(is_Monotonic([1, 2, 3, 0, 1]))
