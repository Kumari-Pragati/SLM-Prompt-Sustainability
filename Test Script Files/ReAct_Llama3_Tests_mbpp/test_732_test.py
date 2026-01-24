import unittest
from mbpp_732_code import replace_specialchar

class TestReplaceSpecialchar(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(replace_specialchar("Hello, world!"), "Hello:, world:")

    def test_edge_case1(self):
        self.assertEqual(replace_specialchar("This is a test."), "This: is: a: test:")

    def test_edge_case2(self):
        self.assertEqual(replace_specialchar("No special characters"), "No special characters")

    def test_edge_case3(self):
        self.assertEqual(replace_specialchar("Only spaces"), "Only: ")

    def test_edge_case4(self):
        self.assertEqual(replace_specialchar("Only commas"), "Only:")

    def test_edge_case5(self):
        self.assertEqual(replace_specialchar("Only dots"), "Only:")

    def test_edge_case6(self):
        self.assertEqual(replace_specialchar("Only commas and spaces"), "Only:")

    def test_edge_case7(self):
        self.assertEqual(replace_specialchar("Multiple special characters"), "Multiple: ")

    def test_edge_case8(self):
        self.assertEqual(replace_specialchar("Multiple special characters with spaces"), "Multiple: ")

    def test_edge_case9(self):
        self.assertEqual(replace_specialchar("Multiple special characters with commas"), "Multiple: ")

    def test_edge_case10(self):
        self.assertEqual(replace_specialchar("Multiple special characters with dots"), "Multiple: ")

    def test_edge_case11(self):
        self.assertEqual(replace_specialchar("Multiple special characters with commas and spaces"), "Multiple: ")

    def test_edge_case12(self):
        self.assertEqual(replace_specialchar("Multiple special characters with commas, dots, and spaces"), "Multiple: ")

    def test_edge_case13(self):
        self.assertEqual(replace_specialchar("Multiple special characters with commas, dots, and spaces with multiple commas"), "Multiple: ")

    def test_edge_case14(self):
        self.assertEqual(replace_specialchar("Multiple special characters with commas, dots, and spaces with multiple dots"), "Multiple: ")

    def test_edge_case15(self):
        self.assertEqual(replace_specialchar("Multiple special characters with commas, dots, and spaces with multiple spaces"), "Multiple: ")

    def test_edge_case16(self):
        self.assertEqual(replace_specialchar("Multiple special characters with commas, dots, and spaces with multiple commas, dots, and spaces"), "Multiple: ")

    def test_edge_case17(self):
        self.assertEqual(replace_specialchar("Multiple special characters with commas, dots, and spaces with multiple commas, dots, and spaces with multiple commas"), "Multiple: ")

    def test_edge_case18(self):
        self.assertEqual(replace_specialchar("Multiple special characters with commas, dots, and spaces with multiple commas, dots, and spaces with multiple dots"), "Multiple: ")

    def test_edge_case19(self):
        self.assertEqual(replace_specialchar("Multiple special characters with commas, dots, and spaces with multiple commas, dots, and spaces with multiple spaces"), "Multiple: ")

    def test_edge_case20(self):
        self.assertEqual(replace_specialchar("Multiple special characters with commas, dots, and spaces with multiple commas, dots, and spaces with multiple commas, dots, and spaces"), "Multiple: ")
