import unittest
from mbpp_542_code import fill_spaces

class TestFillSpaces(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(fill_spaces("Hello, world!"), "Hello:, world:")

    def test_edge_case1(self):
        self.assertEqual(fill_spaces("This is a test."), "This:, is:, a:, test:")

    def test_edge_case2(self):
        self.assertEqual(fill_spaces("No spaces here!"), "No:, spaces:, here!")

    def test_edge_case3(self):
        self.assertEqual(fill_spaces("Multiple spaces   between words"), "Multiple:, spaces:, between:, words")

    def test_edge_case4(self):
        self.assertEqual(fill_spaces("No spaces at all"), "No:, spaces:, at:, all")

    def test_edge_case5(self):
        self.assertEqual(fill_spaces("Only commas,,,,"), "Only:, commas:,,,,")

    def test_edge_case6(self):
        self.assertEqual(fill_spaces("Only dots...."), "Only:, dots:,.,.")

    def test_edge_case7(self):
        self.assertEqual(fill_spaces("Only spaces   "), "Only:, spaces:")

    def test_edge_case8(self):
        self.assertEqual(fill_spaces("Only spaces   between words"), "Only:, spaces:, between:, words")

    def test_edge_case9(self):
        self.assertEqual(fill_spaces("No spaces at all, no commas, no dots"), "No:, spaces:, at:, all, no:, commas:, no:, dots")

    def test_edge_case10(self):
        self.assertEqual(fill_spaces("Multiple spaces   between words, no commas, no dots"), "Multiple:, spaces:, between:, words, no:, commas:, no:, dots")
