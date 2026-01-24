import unittest
from mbpp_173_code import remove_splchar

class TestRemoveSplchar(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(remove_splchar("Hello, World!"), "Hello World")
        self.assertEqual(remove_splchar("1234567890"), "1234567890")
        self.assertEqual(remove_splchar("_abc_123_"), "abc123")

    def test_edge_input(self):
        self.assertEqual(remove_splchar(""), "")
        self.assertEqual(remove_splchar(" "), "")
        self.assertEqual(remove_splchar("_"), "")
        self.assertEqual(remove_splchar("__"), "")
        self.assertEqual(remove_splchar("___"), "")
        self.assertEqual(remove_splchar("____"), "")
        self.assertEqual(remove_splchar("_____"), "")

    def test_boundary_input(self):
        self.assertEqual(remove_splchar("_Hello_"), "Hello")
        self.assertEqual(remove_splchar("Hello_"), "Hello")
        self.assertEqual(remove_splchar("_Hello_World!"), "Hello World")
        self.assertEqual(remove_splchar("Hello_World!"), "Hello World")
        self.assertEqual(remove_splchar("1234567890_"), "1234567890")
        self.assertEqual(remove_splchar("_1234567890"), "1234567890")
        self.assertEqual(remove_splchar("_1234567890_"), "1234567890")

    def test_complex_input(self):
        self.assertEqual(remove_splchar("Hello, World! _123_456_789_012_345_678_901_234_567_890_"),
                         "Hello World 123 456 789 012 345 678 901 234 567 890")
        self.assertEqual(remove_splchar("_123_456_789_012_345_678_901_234_567_890_"), "123 456 789 012 345 678 901 234 567 890")
        self.assertEqual(remove_splchar("_123_456_789_012_345_678_901_234_567_890_ _"), "123 456 789 012 345 678 901 234 567 890 ")
