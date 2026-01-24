import unittest
from mbpp_459_code import remove_uppercase

class TestRemoveUppercase(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(remove_uppercase("Hello World"), "ello world")

    def test_edge_case(self):
        self.assertEqual(remove_uppercase(""), "")

    def test_edge_case2(self):
        self.assertEqual(remove_uppercase("abc"), "abc")

    def test_edge_case3(self):
        self.assertEqual(remove_uppercase("ABC"), "")

    def test_edge_case4(self):
        self.assertEqual(remove_uppercase("aBc"), "bc")

    def test_edge_case5(self):
        self.assertEqual(remove_uppercase("123"), "123")

    def test_edge_case6(self):
        self.assertEqual(remove_uppercase("123ABC"), "123")

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            remove_uppercase(123)
