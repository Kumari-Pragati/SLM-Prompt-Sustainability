import unittest
from mbpp_666_code import count_char

class TestCountChar(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_char('hello', 'l'), 2)

    def test_edge_case(self):
        self.assertEqual(count_char('hello', 'o'), 1)

    def test_edge_case2(self):
        self.assertEqual(count_char('hello', 'h'), 1)

    def test_edge_case3(self):
        self.assertEqual(count_char('hello', 'x'), 0)

    def test_edge_case4(self):
        self.assertEqual(count_char('', 'a'), 0)

    def test_edge_case5(self):
        self.assertEqual(count_char('hello',''), 0)

    def test_edge_case6(self):
        self.assertEqual(count_char('hello', 'hj'), 0)

    def test_edge_case7(self):
        self.assertEqual(count_char('hello', 'h'), 1)

    def test_edge_case8(self):
        self.assertEqual(count_char('hello', 'o'), 1)

    def test_edge_case9(self):
        self.assertEqual(count_char('hello', 'l'), 2)

    def test_edge_case10(self):
        self.assertEqual(count_char('hello', 'o'), 1)

    def test_edge_case11(self):
        self.assertEqual(count_char('hello', 'o'), 1)

    def test_edge_case12(self):
        self.assertEqual(count_char('hello', 'o'), 1)

    def test_edge_case13(self):
        self.assertEqual(count_char('hello', 'o'), 1)

    def test_edge_case14(self):
        self.assertEqual(count_char('hello', 'o'), 1)

    def test_edge_case15(self):
        self.assertEqual(count_char('hello', 'o'), 1)
