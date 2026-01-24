import unittest
from mbpp_713_code import check_valid

class TestCheckValid(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertTrue(check_valid((True, True, True)))

    def test_edge_condition(self):
        self.assertTrue(check_valid((False, True, True)))

    def test_boundary_condition(self):
        self.assertFalse(check_valid((False, False, False)))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            check_valid((True, "string", True))
