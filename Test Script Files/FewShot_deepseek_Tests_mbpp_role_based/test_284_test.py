import unittest
from mbpp_284_code import check_element

class TestCheckElement(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertTrue(check_element([1, 1, 1], 1))

    def test_edge_condition(self):
        self.assertTrue(check_element([], 1))

    def test_boundary_condition(self):
        self.assertFalse(check_element([1, 2, 3], 2))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            check_element("1, 2, 3", 1)
