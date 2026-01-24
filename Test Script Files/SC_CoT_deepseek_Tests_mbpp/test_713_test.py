import unittest
from mbpp_713_code import check_valid

class TestCheckValid(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(check_valid((True, True, True)))

    def test_edge_case(self):
        self.assertFalse(check_valid((False, False, False)))

    def test_boundary_case(self):
        self.assertFalse(check_valid((False, True, False)))

    def test_special_case(self):
        self.assertTrue(check_valid((True, False, True)))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            check_valid((True, True, 'a'))
