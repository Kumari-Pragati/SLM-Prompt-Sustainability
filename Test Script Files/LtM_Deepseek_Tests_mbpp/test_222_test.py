import unittest
from mbpp_222_code import check_type

class TestCheckType(unittest.TestCase):

    def test_simple_valid_inputs(self):
        self.assertTrue(check_type((1, 2, 3)))
        self.assertTrue(check_type(('a', 'b', 'c')))
        self.assertTrue(check_type((True, False, True)))

    def test_edge_conditions(self):
        self.assertTrue(check_type(()))
        self.assertTrue(check_type((1,)))
        self.assertTrue(check_type(('a',)))

    def test_complex_cases(self):
        self.assertFalse(check_type((1, 'a', True)))
        self.assertFalse(check_type((1, 2, 'a')))
        self.assertFalse(check_type((True, False, 1)))
