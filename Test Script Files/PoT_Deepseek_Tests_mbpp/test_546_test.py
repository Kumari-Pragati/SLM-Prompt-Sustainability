import unittest
from mbpp_546_code import last_occurence_char

class TestLastOccurenceChar(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(last_occurence_char("hello", "l"), 3)
        self.assertEqual(last_occurence_char("world", "o"), 5)
        self.assertEqual(last_occurence_char("abcabc", "b"), 6)

    def test_edge_cases(self):
        self.assertEqual(last_occurence_char("", "a"), None)
        self.assertEqual(last_occurence_char("a", "a"), 2)
        self.assertEqual(last_occurence_char("a", "b"), None)

    def test_boundary_cases(self):
        self.assertEqual(last_occurence_char("a"*100000, "a"), 100001)
        self.assertEqual(last_occurence_char("b"*100000, "a"), None)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            last_occurence_char(12345, "a")
        with self.assertRaises(TypeError):
            last_occurence_char("hello", 12345)
