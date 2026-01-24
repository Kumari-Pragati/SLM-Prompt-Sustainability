import unittest
from mbpp_192_code import check_String

class TestCheckString(unittest.TestCase):
    def test_typical_cases(self):
        self.assertTrue(check_String("A1B2C3"))
        self.assertTrue(check_String("1a2b3c"))
        self.assertTrue(check_String("Ab1c2D3"))
        self.assertTrue(check_String("1A2B3C"))

    def test_edge_cases(self):
        self.assertFalse(check_String(""))
        self.assertFalse(check_String("A"))
        self.assertFalse(check_String("1"))
        self.assertFalse(check_String("A1"))

    def test_corner_cases(self):
        self.assertFalse(check_String("A1B!2C3"))
        self.assertFalse(check_String("1A2B!3C"))
        self.assertFalse(check_String("A1B2C!3"))
        self.assertFalse(check_String("1A2B!C3"))
