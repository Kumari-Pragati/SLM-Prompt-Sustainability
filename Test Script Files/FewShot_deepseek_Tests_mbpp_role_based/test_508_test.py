import unittest
from mbpp_508_code import same_order

class TestSameOrder(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertTrue(same_order([1, 2, 3], [3, 2, 1]))

    def test_edge_case_empty_lists(self):
        self.assertTrue(same_order([], []))

    def test_boundary_case_one_empty_list(self):
        self.assertFalse(same_order([1, 2, 3], []))
        self.assertFalse(same_order([], [1, 2, 3]))

    def test_boundary_case_same_elements_different_order(self):
        self.assertFalse(same_order([1, 2, 3], [3, 1, 2]))

    def test_boundary_case_same_elements_same_order(self):
        self.assertTrue(same_order([1, 2, 3], [1, 2, 3]))

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            same_order("1, 2, 3", [1, 2, 3])
        with self.assertRaises(TypeError):
            same_order([1, 2, 3], "1, 2, 3")
