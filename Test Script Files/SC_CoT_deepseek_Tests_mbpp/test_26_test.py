import unittest
from mbpp_26_code import check_k_elements

class TestCheckKElements(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(check_k_elements([(1, 2, 3), (4, 5, 6)], 7))

    def test_edge_case(self):
        self.assertFalse(check_k_elements([(1, 2, 3), (4, 5, 6)], 6))

    def test_boundary_case(self):
        self.assertFalse(check_k_elements([(1, 2, 3), (4, 5, 6)], 5))

    def test_special_case(self):
        self.assertFalse(check_k_elements([(1, 2, 3), (4, 5, 6)], 1))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            check_k_elements("not a list", 1)
