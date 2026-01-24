import unittest
from mbpp_192_code import check_String

class TestCheckString(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertTrue(check_String("Hello123"))
        self.assertTrue(check_String("World456"))
        self.assertTrue(check_String("abc123"))

    def test_edge_cases(self):
        self.assertFalse(check_String("123"))
        self.assertFalse(check_String("abc"))
        self.assertFalse(check_String(""))

    def test_boundary_cases(self):
        self.assertTrue(check_String("a1b2c3"))
        self.assertTrue(check_String("A1B2C3"))
        self.assertTrue(check_String("aBcD"))

    def test_special_cases(self):
        self.assertFalse(check_String("123abc"))
        self.assertFalse(check_String("abc123"))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            check_String(123)
        with self.assertRaises(TypeError):
            check_String(None)
