import unittest
from mbpp_334_code import check_Validity

class TestCheckValidity(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(check_Validity(3, 4, 5))

    def test_boundary_condition(self):
        self.assertFalse(check_Validity(0, 0, 0))

    def test_edge_case(self):
        self.assertFalse(check_Validity(1, 1, 3))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            check_Validity("a", 1, 2)
