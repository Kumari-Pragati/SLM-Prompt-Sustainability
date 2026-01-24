import unittest
from mbpp_546_code import last_occurence_char

class TestLastOccurenceChar(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(last_occurence_char("hello", 'o'), 3)

    def test_edge_case(self):
        self.assertEqual(last_occurence_char("hello", 'h'), 0)

    def test_edge_case2(self):
        self.assertEqual(last_occurence_char("hello", 'x'), None)

    def test_edge_case3(self):
        self.assertEqual(last_occurence_char("", 'a'), None)

    def test_edge_case4(self):
        self.assertEqual(last_occurence_char("hello", 'l'), 2)

    def test_edge_case5(self):
        self.assertEqual(last_occurence_char("hello", 'o'), 3)

    def test_edge_case6(self):
        self.assertEqual(last_occurence_char("hello", 'o'), 3)

    def test_edge_case7(self):
        self.assertEqual(last_occurence_char("hello", 'o'), 3)

    def test_edge_case8(self):
        self.assertEqual(last_occurence_char("hello", 'o'), 3)

    def test_edge_case9(self):
        self.assertEqual(last_occurence_char("hello", 'o'), 3)

    def test_edge_case10(self):
        self.assertEqual(last_occurence_char("hello", 'o'), 3)
