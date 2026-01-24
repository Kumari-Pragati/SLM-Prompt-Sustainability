import unittest
from mbpp_192_code import check_String

class TestCheckString(unittest.TestCase):

    def test_simple_string(self):
        self.assertTrue(check_String("A1"))
        self.assertTrue(check_String("1A"))

    def test_edge_cases(self):
        self.assertFalse(check_String(""))
        self.assertFalse(check_String("A"))
        self.assertFalse(check_String("1"))
        self.assertFalse(check_String("A123456789"))
        self.assertFalse(check_String("123456789A"))

    def test_complex_cases(self):
        self.assertTrue(check_String("A1B2C3"))
        self.assertTrue(check_String("1A2B3C4"))
        self.assertFalse(check_String("A1B2C3D"))
        self.assertFalse(check_String("1A2B3C4D"))
