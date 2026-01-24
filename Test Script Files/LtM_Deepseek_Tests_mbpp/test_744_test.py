import unittest
from mbpp_744_code import check_none

class TestCheckNone(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertFalse(check_none((1, 2, 3)))
        self.assertFalse(check_none(('a', 'b', 'c')))
        self.assertFalse(check_none((True, False, True)))

    def test_edge_conditions(self):
        self.assertFalse(check_none(()))
        self.assertFalse(check_none((None,)))
        self.assertTrue(check_none((None, None, None)))

    def test_complex_cases(self):
        self.assertTrue(check_none((None, 1, 2, 3)))
        self.assertTrue(check_none((1, 2, None, 3)))
        self.assertTrue(check_none((1, 2, 3, None)))
        self.assertTrue(check_none((1, None, 2, None, 3)))
