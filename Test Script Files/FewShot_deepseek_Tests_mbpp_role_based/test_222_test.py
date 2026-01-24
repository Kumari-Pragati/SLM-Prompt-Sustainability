import unittest
from mbpp_222_code import check_type

class TestCheckType(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertTrue(check_type((1, 2, 3)))

    def test_edge_condition(self):
        self.assertTrue(check_type((1,)))

    def test_boundary_condition(self):
        self.assertTrue(check_type(()))
        self.assertFalse(check_type((1, 2, '3')))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            check_type(1)
