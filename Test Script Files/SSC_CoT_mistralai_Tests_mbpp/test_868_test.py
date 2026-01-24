import unittest
from mbpp_868_code import length_Of_Last_Word

class TestLengthOfLastWord(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(length_Of_Last_Word("hello world"), 5)
        self.assertEqual(length_Of_Last_Word("I am a test"), 5)
        self.assertEqual(length_Of_Last_Word("This is a test"), 4)

    def test_edge_cases(self):
        self.assertEqual(length_Of_Last_Word(""), 0)
        self.assertEqual(length_Of_Last_Word(" "), 0)
        self.assertEqual(length_Of_Last_Word("hello"), 5)
        self.assertEqual(length_Of_Last_Word("world"), 5)
        self.assertEqual(length_Of_Last_Word("hello world "), 5)
        self.assertEqual(length_Of_Last_Word("hello\tworld"), 5)
        self.assertEqual(length_Of_Last_Word("hello\nworld"), 5)

    def test_boundary_cases(self):
        self.assertEqual(length_Of_Last_Word("hello world\t"), 5)
        self.assertEqual(length_Of_Last_Word("hello world\n"), 5)
        self.assertEqual(length_Of_Last_Word("hello world\r"), 5)
        self.assertEqual(length_Of_Last_Word("\thello world"), 5)
        self.assertEqual(length_Of_Last_Word("\nhello world"), 5)
        self.assertEqual(length_Of_Last_Word("\rhello world"), 5)
