import unittest
from mbpp_868_code import length_OfLastWord

class TestLengthOfLastWord(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(length_OfLastWord("hello world"), 5)
        self.assertEqual(length_OfLastWord("hello"), 5)
        self.assertEqual(length_OfLastWord("world"), 5)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(length_OfLastWord(""), 0)
        self.assertEqual(length_OfLastWord(" "), 0)
        self.assertEqual(length_OfLastWord("hello world "), 5)
        self.assertEqual(length_OfLastWord("hello world\t"), 5)
        self.assertEqual(length_OfLastWord("hello\nworld"), 5)
        self.assertEqual(length_OfLastWord("hello\rworld"), 5)
        self.assertEqual(length_OfLastWord("hello\r\nworld"), 5)

    def test_complex_scenarios(self):
        self.assertEqual(length_OfLastWord("hello world!"), 5)
        self.assertEqual(length_OfLastWord("hello world! "), 5)
        self.assertEqual(length_OfLastWord("hello world!   "), 5)
        self.assertEqual(length_OfLastWord("hello world!   \t"), 5)
        self.assertEqual(length_OfLastWord("hello world!   \t\n"), 5)
        self.assertEqual(length_OfLastWord("hello world!   \t\n\r"), 5)
        self.assertEqual(length_OfLastWord("hello world!   \t\n\r\n"), 5)
