import unittest
from mbpp_546_code import last_occurence_char

class TestLastOccurenceChar(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(last_occurence_char("hello", "l"), 4)
        self.assertEqual(last_occurence_char("Python", "n"), 5)
        self.assertEqual(last_occurence_char("12345", "5"), 4)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(last_occurence_char("", "a"), None)
        self.assertEqual(last_occurence_char("a", "z"), 0)
        self.assertEqual(last_occurence_char("zzz", "a"), None)
        self.assertEqual(last_occurence_char("aa", "b"), None)

    def test_complex_scenarios(self):
        self.assertEqual(last_occurence_char("Python", "y"), None)
        self.assertEqual(last_occurence_char("Python", "P"), 0)
        self.assertEqual(last_occurence_char("Python", "h"), 3)
        self.assertEqual(last_occurence_char("Python", "T"), None)
