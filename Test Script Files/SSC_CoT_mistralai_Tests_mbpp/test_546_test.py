import unittest
from mbpp_546_code import last_occurence_char

class TestLastOccurenceChar(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(last_occurence_char("hello", "l"), 4)
        self.assertEqual(last_occurence_char("Python", "n"), 5)
        self.assertEqual(last_occurence_char("12345", "5"), 4)

    def test_edge_and_boundary_cases(self):
        self.assertEqual(last_occurence_char("", "a"), None)
        self.assertEqual(last_occurence_char("abc", "d"), None)
        self.assertEqual(last_occurence_char("abc", "a"), 0)
        self.assertEqual(last_occurence_char("aaa", "a"), 2)
        self.assertEqual(last_occurence_char("aa", "a"), 1)
        self.assertEqual(last_occurence_char("a", "a"), None)

    def test_special_cases(self):
        self.assertEqual(last_occurence_char("Python", "y"), None)
        self.assertEqual(last_occurence_char("Python", "P"), 0)
        self.assertEqual(last_occurence_char("Python", "h"), 3)
        self.assertEqual(last_occurence_char("Python", "T"), None)
