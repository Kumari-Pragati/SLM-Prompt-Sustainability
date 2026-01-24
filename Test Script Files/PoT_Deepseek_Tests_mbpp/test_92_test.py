import unittest
from mbpp_92_code import is_undulating

class TestIsUndulating(unittest.TestCase):

    def test_typical_cases(self):
        self.assertTrue(is_undulating('11'))
        self.assertTrue(is_undulating('2222'))
        self.assertTrue(is_undulating('333333'))
        self.assertTrue(is_undulating('44444444'))
        self.assertTrue(is_undulating('5555555555'))

    def test_edge_cases(self):
        self.assertFalse(is_undulating(''))
        self.assertFalse(is_undulating('1'))
        self.assertFalse(is_undulating('111'))
        self.assertFalse(is_undulating('22222'))

    def test_boundary_conditions(self):
        self.assertTrue(is_undulating('121212'))
        self.assertFalse(is_undulating('123123'))
        self.assertFalse(is_undulating('12123123'))

    def test_corner_cases(self):
        self.assertFalse(is_undulating('12345'))
        self.assertFalse(is_undulating('1122334455'))
        self.assertFalse(is_undulating('111222333444'))
