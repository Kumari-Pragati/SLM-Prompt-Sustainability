import unittest
from mbpp_868_code import length_Of_Last_Word

class TestLengthOfLastWord(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(length_Of_Last_Word("Hello World"), 5)
        self.assertEqual(length_Of_Last_Word("a"), 1)

    def test_edge_conditions(self):
        self.assertEqual(length_Of_Last_Word(""), 0)
        self.assertEqual(length_Of_Last_Word("   "), 0)
        self.assertEqual(length_Of_Last_Word("   a   "), 1)

    def test_complex_cases(self):
        self.assertEqual(length_Of_Last_Word("Hello   World"), 5)
        self.assertEqual(length_Of_Last_Word("a b c d e f g h i j k l m n o p q r s t u v w x y z"), 1)
