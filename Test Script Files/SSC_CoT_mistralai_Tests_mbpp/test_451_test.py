import unittest
from mbpp_451_code import remove_whitespaces

class TestRemoveWhitespaces(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(remove_whitespaces("Hello World"), "HelloWorld")

    def test_edge_input(self):
        self.assertEqual(remove_whitespaces(" "), "")
        self.assertEqual(remove_whitespaces("\tHello World"), "HelloWorld")
        self.assertEqual(remove_whitespaces("\nHello World"), "HelloWorld")
        self.assertEqual(remove_whitespaces("\rHello World"), "HelloWorld")

    def test_boundary_input(self):
        self.assertEqual(remove_whitespaces("Hello World\t"), "HelloWorld")
        self.assertEqual(remove_whitespaces("Hello World\n"), "HelloWorld")
        self.assertEqual(remove_whitespaces("Hello World\r"), "HelloWorld")

    def test_special_input(self):
        self.assertEqual(remove_whitespaces("Hello World!!"), "HelloWorld!")
        self.assertEqual(remove_whitespaces("Hello World_"), "HelloWorld")
        self.assertEqual(remove_whitespaces("Hello World-"), "HelloWorld")
        self.assertEqual(remove_whitespaces("Hello World@"), "HelloWorld")
        self.assertEqual(remove_whitespaces("Hello World#"), "HelloWorld")
        self.assertEqual(remove_whitespaces("Hello World$"), "HelloWorld")
        self.assertEqual(remove_whitespaces("Hello World%"), "HelloWorld")
        self.assertEqual(remove_whitespaces("Hello World&"), "HelloWorld")
        self.assertEqual(remove_whitespaces("Hello World'"), "HelloWorld")
        self.assertEqual(remove_whitespaces("Hello World\""), "HelloWorld")
        self.assertEqual(remove_whitespaces("Hello World^"), "HelloWorld")
        self.assertEqual(remove_whitespaces("Hello World_"), "HelloWorld")
        self.assertEqual(remove_whitespaces("Hello World~"), "HelloWorld")
