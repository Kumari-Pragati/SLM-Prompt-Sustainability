import unittest
from mbpp_546_code import last_occurence_char

class TestLastOccurenceChar(unittest.TestCase):

    def test_last_occurence_char(self):
        self.assertEqual(last_occurence_char("hello", 'o'), 4)
        self.assertEqual(last_occurence_char("hello", 'h'), 0)
        self.assertEqual(last_occurence_char("hello", 'x'), None)
        self.assertEqual(last_occurence_char("abc", 'a'), 0)
        self.assertEqual(last_occurence_char("abc", 'b'), 1)
        self.assertEqual(last_occurence_char("abc", 'c'), 2)
        self.assertEqual(last_occurence_char("abc", 'd'), None)
        self.assertEqual(last_occurence_char("", 'a'), None)
        self.assertEqual(last_occurence_char("a", 'a'), 0)
        self.assertEqual(last_occurence_char("a", 'b'), None)
