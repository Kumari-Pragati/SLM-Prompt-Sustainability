import unittest
from mbpp_459_code import remove_uppercase

class TestRemoveUppercase(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(remove_uppercase("Hello World"), "hello world")
        self.assertEqual(remove_uppercase("123ABC456"), "123456")
        self.assertEqual(remove_uppercase("HELLO_WORLD"), "hello_world")

    def test_edge_case(self):
        self.assertEqual(remove_uppercase(""), "")
        self.assertEqual(remove_uppercase("A"), "")
        self.assertEqual(remove_uppercase("a"), "a")
        self.assertEqual(remove_uppercase("AB"), "b")
        self.assertEqual(remove_uppercase("Z"), "")

    def test_corner_case(self):
        self.assertEqual(remove_uppercase("A-B"), "A-b")
        self.assertEqual(remove_uppercase("1A2B3"), "12b3")
        self.assertEqual(remove_uppercase("_A_"), "_")
        self.assertEqual(remove_uppercase("A_B"), "a_b")
