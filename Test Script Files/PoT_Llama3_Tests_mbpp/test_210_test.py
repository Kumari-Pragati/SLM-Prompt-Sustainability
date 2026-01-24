import unittest
from mbpp_210_code import is_allowed_specific_char

class TestIsAllowedSpecificChar(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(is_allowed_specific_char("hello"))
        self.assertTrue(is_allowed_specific_char("12345"))
        self.assertTrue(is_allowed_specific_char("hello.12345"))

    def test_edge_case(self):
        self.assertFalse(is_allowed_specific_char("hello!"))
        self.assertFalse(is_allowed_specific_char("12345!"))
        self.assertFalse(is_allowed_specific_char("hello.12345!"))

    def test_edge_case2(self):
        self.assertFalse(is_allowed_specific_char("hello,"))
        self.assertFalse(is_allowed_specific_char("12345,"))
        self.assertFalse(is_allowed_specific_char("hello.12345,"))

    def test_edge_case3(self):
        self.assertFalse(is_allowed_specific_char("hello-"))
        self.assertFalse(is_allowed_specific_char("12345-"))
        self.assertFalse(is_allowed_specific_char("hello.12345-"))

    def test_edge_case4(self):
        self.assertFalse(is_allowed_specific_char("hello_"))
        self.assertFalse(is_allowed_specific_char("12345_"))
        self.assertFalse(is_allowed_specific_char("hello.12345_"))

    def test_edge_case5(self):
        self.assertFalse(is_allowed_specific_char("hello "))
        self.assertFalse(is_allowed_specific_char("12345 "))
        self.assertFalse(is_allowed_specific_char("hello.12345 "))

    def test_edge_case6(self):
        self.assertFalse(is_allowed_specific_char("hello! "))
        self.assertFalse(is_allowed_specific_char("12345! "))
        self.assertFalse(is_allowed_specific_char("hello.12345! "))

    def test_edge_case7(self):
        self.assertFalse(is_allowed_specific_char("hello, "))
        self.assertFalse(is_allowed_specific_char("12345, "))
        self.assertFalse(is_allowed_specific_char("hello.12345, "))

    def test_edge_case8(self):
        self.assertFalse(is_allowed_specific_char("hello- "))
        self.assertFalse(is_allowed_specific_char("12345- "))
        self.assertFalse(is_allowed_specific_char("hello.12345- "))

    def test_edge_case9(self):
        self.assertFalse(is_allowed_specific_char("hello_ "))
        self.assertFalse(is_allowed_specific_char("12345_ "))
        self.assertFalse(is_allowed_specific_char("hello.12345_ "))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            is_allowed_specific_char(None)
