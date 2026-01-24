import unittest
from mbpp_744_code import check_none

class TestCheckNone(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertTrue(check_none((1, 2, None)))

    def test_edge_condition(self):
        self.assertFalse(check_none((1, 2, 3)))

    def test_boundary_condition(self):
        self.assertFalse(check_none(()))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            check_none(123)
