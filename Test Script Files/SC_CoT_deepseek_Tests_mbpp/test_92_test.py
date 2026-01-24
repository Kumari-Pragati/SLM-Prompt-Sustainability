import unittest
from mbpp_92_code import is_undulating

class TestIsUndulating(unittest.TestCase):

    def test_typical_cases(self):
        self.assertTrue(is_undulating('1122'))
        self.assertTrue(is_undulating('1234321'))
        self.assertTrue(is_undulating('12121212'))

    def test_edge_cases(self):
        self.assertFalse(is_undulating(''))
        self.assertFalse(is_undulating('1'))
        self.assertFalse(is_undulating('11'))
        self.assertFalse(is_undulating('111'))

    def test_corner_cases(self):
        self.assertFalse(is_undulating('123'))
        self.assertFalse(is_undulating('11223'))
        self.assertFalse(is_undulating('12345'))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            is_undulating(123)
        with self.assertRaises(TypeError):
            is_undulating(None)
        with self.assertRaises(TypeError):
            is_undulating([])
