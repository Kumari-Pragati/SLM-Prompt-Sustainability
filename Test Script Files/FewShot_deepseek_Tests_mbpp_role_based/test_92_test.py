import unittest
from mbpp_92_code import is_undulating

class TestIsUndulating(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(is_undulating('11'))
        self.assertTrue(is_undulating('1212'))
        self.assertTrue(is_undulating('123123'))

    def test_edge_case(self):
        self.assertFalse(is_undulating(''))
        self.assertFalse(is_undulating('1'))
        self.assertFalse(is_undulating('111'))

    def test_boundary_case(self):
        self.assertTrue(is_undulating('1111'))
        self.assertFalse(is_undulating('12'))
        self.assertFalse(is_undulating('123'))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            is_undulating(123)
        with self.assertRaises(TypeError):
            is_undulating(123456)
