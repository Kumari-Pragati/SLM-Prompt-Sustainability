import unittest
from mbpp_868_code import length_Of_Last_Word

class TestLengthOfLastWord(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(length_Of_Last_Word("Hello"), 5)
        self.assertEqual(length_Of_Last_Word("World"), 5)
        self.assertEqual(length_Of_Last_Word("Python"), 6)

    def test_edge_cases(self):
        self.assertEqual(length_Of_Last_Word(""), 0)
        self.assertEqual(length_Of_Last_Word("   "), 0)
        self.assertEqual(length_Of_Last_Word("a"), 1)
        self.assertEqual(length_Of_Last_Word("abc"), 3)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            length_Of_Last_Word(None)
        with self.assertRaises(TypeError):
            length_Of_Last_Word(123)
