import unittest
from mbpp_772_code import remove_length

class TestRemoveLength(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(remove_length("Hello World", 5), "Hello World")

    def test_edge_case1(self):
        self.assertEqual(remove_length("Hello", 5), "Hello")

    def test_edge_case2(self):
        self.assertEqual(remove_length("Hello World", 1), "Hello World")

    def test_edge_case3(self):
        self.assertEqual(remove_length("Hello World", 11), "")

    def test_edge_case4(self):
        self.assertEqual(remove_length("Hello World", 0), "Hello World")

    def test_edge_case5(self):
        self.assertEqual(remove_length("Hello World", 12), "")

    def test_error_case1(self):
        with self.assertRaises(TypeError):
            remove_length(None, 5)

    def test_error_case2(self):
        with self.assertRaises(TypeError):
            remove_length("Hello World", None)

    def test_error_case3(self):
        with self.assertRaises(TypeError):
            remove_length(123, 5)

    def test_error_case4(self):
        with self.assertRaises(TypeError):
            remove_length("Hello World", "five")
