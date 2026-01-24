import unittest
from mbpp_210_code import is_allowed_specific_char

class TestIsAllowedSpecificChar(unittest.TestCase):

    def test_typical_cases(self):
        self.assertTrue(is_allowed_specific_char('abc123.def'))
        self.assertTrue(is_allowed_specific_char(''))

    def test_edge_cases(self):
        self.assertTrue(is_allowed_specific_char('a1.'))
        self.assertFalse(is_allowed_specific_char('a1@'))
        self.assertFalse(is_allowed_specific_char('a1@.'))
        self.assertFalse(is_allowed_specific_char('a1@.b'))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            is_allowed_specific_char(123)
        with self.assertRaises(TypeError):
            is_allowed_specific_char(None)
        with self.assertRaises(TypeError):
            is_allowed_specific_char(True)
        with self.assertRaises(TypeError):
            is_allowed_specific_char([1, 2, 3])
