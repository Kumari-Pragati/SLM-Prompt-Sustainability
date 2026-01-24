import unittest
from mbpp_394_code import check_distinct

class TestCheckDistinct(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertTrue(check_distinct((1, 2, 3)))
        self.assertTrue(check_distinct(('a', 'b', 'c')))
        self.assertTrue(check_distinct((True, False)))

    def test_edge_conditions(self):
        self.assertTrue(check_distinct(()))
        self.assertTrue(check_distinct((1,)))
        self.assertTrue(check_distinct(('a',)))
        self.assertTrue(check_distinct((True,)))

    def test_complex_cases(self):
        self.assertFalse(check_distinct((1, 2, 1)))
        self.assertFalse(check_distinct((True, False, True)))
        self.assertFalse(check_distinct((1, 'a', 1)))
        self.assertFalse(check_distinct((True, 'a', True)))
