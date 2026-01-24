import unittest
from mbpp_222_code import check_type

class TestCheckType(unittest.TestCase):

    def test_simple_valid_inputs(self):
        self.assertTrue(check_type((1, 1)))
        self.assertTrue(check_type((3.14, 3.14)))
        self.assertTrue(check_type(('a', 'a')))

    def test_edge_and_boundary_conditions(self):
        self.assertFalse(check_type((1, 2, 3)))
        self.assertFalse(check_type((1,)))
        self.assertFalse(check_type((1, None)))
        self.assertFalse(check_type((1, 1.0)))
        self.assertFalse(check_type(('a', 1)))

    def test_complex_and_corner_cases(self):
        self.assertTrue(check_type((1, 1, 1, 1)))
        self.assertTrue(check_type((1, 1, 1, 2)))
        self.assertFalse(check_type((1, 1, 'a')))
        self.assertFalse(check_type((1, 1, 1, None)))
        self.assertFalse(check_type((1, 1.0, 1)))
        self.assertFalse(check_type((1, 1, 'a', 'a')))
