import unittest
from mbpp_192_code import check_String

class TestCheckString(unittest.TestCase):
    def test_typical_strings(self):
        self.assertTrue(check_String("Hello123"))
        self.assertTrue(check_String("abc456"))
        self.assertTrue(check_String("helloWorld123"))

    def test_edge_cases(self):
        self.assertFalse(check_String("123"))
        self.assertFalse(check_String("abc"))
        self.assertFalse(check_String(""))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            check_String(123)
        with self.assertRaises(TypeError):
            check_String(None)
        with self.assertRaises(TypeError):
            check_String([1, 2, 3])

    def test_boundary_cases(self):
        self.assertTrue(check_String("a1b2c3"))
        self.assertTrue(check_String("Hello123World"))
