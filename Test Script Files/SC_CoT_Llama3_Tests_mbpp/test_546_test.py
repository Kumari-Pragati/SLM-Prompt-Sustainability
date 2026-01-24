import unittest
from mbpp_546_code import last_occurence_char

class TestLastOccurenceChar(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(last_occurence_char("hello world", "o"), 7)

    def test_edge_case(self):
        self.assertEqual(last_occurence_char("hello world", "o"), 7)
        self.assertEqual(last_occurence_char("hello world", "H"), None)

    def test_edge_case2(self):
        self.assertEqual(last_occurence_char("", "o"), None)
        self.assertEqual(last_occurence_char("hello world", "z"), None)

    def test_edge_case3(self):
        self.assertEqual(last_occurence_char("hello world", "o"), 7)
        self.assertEqual(last_occurence_char("hello world", "W"), None)

    def test_edge_case4(self):
        self.assertEqual(last_occurence_char("hello world", "o"), 7)
        self.assertEqual(last_occurence_char("hello world", "x"), None)

    def test_edge_case5(self):
        self.assertEqual(last_occurence_char("hello world", "o"), 7)
        self.assertEqual(last_occurence_char("hello world", "a"), None)

    def test_edge_case6(self):
        self.assertEqual(last_occurence_char("hello world", "o"), 7)
        self.assertEqual(last_occurence_char("hello world", "b"), None)

    def test_edge_case7(self):
        self.assertEqual(last_occurence_char("hello world", "o"), 7)
        self.assertEqual(last_occurence_char("hello world", "c"), None)

    def test_edge_case8(self):
        self.assertEqual(last_occurence_char("hello world", "o"), 7)
        self.assertEqual(last_occurence_char("hello world", "d"), None)

    def test_edge_case9(self):
        self.assertEqual(last_occurence_char("hello world", "o"), 7)
        self.assertEqual(last_occurence_char("hello world", "e"), None)

    def test_edge_case10(self):
        self.assertEqual(last_occurence_char("hello world", "o"), 7)
        self.assertEqual(last_occurence_char("hello world", "f"), None)

    def test_edge_case11(self):
        self.assertEqual(last_occurence_char("hello world", "o"), 7)
        self.assertEqual(last_occurence_char("hello world", "g"), None)

    def test_edge_case12(self):
        self.assertEqual(last_occurence_char("hello world", "o"), 7)
        self.assertEqual(last_occurence_char("hello world", "h"), None)

    def test_edge_case13(self):
        self.assertEqual(last_occurence_char("hello world", "o"), 7)
        self.assertEqual(last_occurence_char("hello world", "i"), None)

    def test_edge_case14(self):
        self.assertEqual(last_occurence_char("hello world", "o"), 7)
        self.assertEqual(last_occurence_char("hello world", "j"), None)

    def test_edge_case15(self):
        self.assertEqual(last_occurence_char("hello world", "o"), 7)
        self.assertEqual(last_occurence_char("hello world", "k"), None)

    def test_edge_case16(self):
        self.assertEqual(last_occurence_char("hello world", "o"), 7)
        self.assertEqual(last_occurence_char("hello world", "l"), None)

    def test_edge_case17(self):
        self.assertEqual(last_occurence_char("hello world", "o"), 7)
        self.assertEqual(last_occurence_char("hello world", "m"), None)

    def test_edge_case18(self):
        self.assertEqual(last_occurence_char("hello world", "o"), 7)
        self.assertEqual(last_occurence_char("hello world", "n"), None)

    def test_edge_case19(self):
        self.assertEqual(last_occurence_char("hello world", "o"), 7)
        self.assertEqual(last_occurence_char("hello world", "o"), 7)

    def test_edge_case20(self):
        self.assertEqual(last_occurence_char("hello world", "o"), 7)
        self.assertEqual(last_occurence_char("hello world", "p"), None)

    def test_edge_case21(self):
        self.assertEqual(last_occurence_char("hello world", "o"), 7)
        self.assertEqual(last_occurence_char("hello world", "q"), None)

    def test_edge_case22(self):
        self.assertEqual(last_occurence_char("hello world", "o"), 7)
        self.assertEqual(last_occurence_char("hello world", "r"), None)

    def test_edge_case23(self):
        self.assertEqual(last_occurence_char("hello world", "o"), 7)
        self.assertEqual(last_occurence_char("hello world", "s"), None)

    def test_edge_case24(self):
        self.assertEqual(last_occurence_char("hello world", "o"), 7)
        self.assertEqual(last_occurence_char("hello world", "t