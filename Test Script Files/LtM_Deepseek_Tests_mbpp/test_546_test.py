import unittest
from mbpp_546_code import last_occurence_char

class TestLastOccurenceChar(unittest.TestCase):

    # Test for simple / typical inputs
    def test_typical_inputs(self):
        self.assertEqual(last_occurence_char("hello", "l"), 5)
        self.assertEqual(last_occurence_char("world", "o"), 6)

    # Test for edge and boundary conditions
    def test_edge_conditions(self):
        self.assertEqual(last_occurence_char("", "a"), None)
        self.assertEqual(last_occurence_char("a", "a"), 2)
        self.assertEqual(last_occurence_char("a", "b"), None)

    # Test for more complex or corner cases
    def test_complex_cases(self):
        self.assertEqual(last_occurence_char("aaa", "a"), 3)
        self.assertEqual(last_occurence_char("abc", "d"), None)
        self.assertEqual(last_occurence_char("abcabc", "b"), 6)
