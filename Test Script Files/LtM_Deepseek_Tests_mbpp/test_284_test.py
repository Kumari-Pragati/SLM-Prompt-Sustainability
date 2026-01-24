import unittest
from mbpp_284_code import check_element

class TestCheckElement(unittest.TestCase):

    def test_simple_valid_input(self):
        self.assertTrue(check_element([1, 1, 1], 1))

    def test_edge_case_empty_list(self):
        self.assertTrue(check_element([], 1))
        self.assertTrue(check_element([], None))

    def test_boundary_case_single_element(self):
        self.assertTrue(check_element([1], 1))
        self.assertFalse(check_element([1], 2))

    def test_complex_case_mixed_elements(self):
        self.assertFalse(check_element([1, 2, 3], 2))
        self.assertFalse(check_element([1, 2, 3], 4))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            check_element("not a list", 1)
