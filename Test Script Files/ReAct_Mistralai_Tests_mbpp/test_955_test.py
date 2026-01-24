import unittest
from mbpp_955_code import is_abundant

class TestIsAbundant(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(is_abundant(12))
        self.assertTrue(is_abundant(28))

    def test_edge_case_start(self):
        self.assertFalse(is_abundant(1))
        self.assertFalse(is_abundant(2))

    def test_edge_case_end(self):
        self.assertTrue(is_abundant(29))
        self.assertTrue(is_abundant(30))

    def test_boundary_cases(self):
        self.assertTrue(is_abundant(120))
        self.assertFalse(is_abundant(121))

    def test_error_handling(self):
        self.assertRaises(TypeError, is_abundant, 'not_a_number')
