import unittest
from mbpp_165_code import count_char_position

class TestCountCharPosition(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_char_position("Hello, World!"), 2)

    def test_edge_case1(self):
        self.assertEqual(count_char_position("abc"), 0)

    def test_edge_case2(self):
        self.assertEqual(count_char_position("ABC"), 0)

    def test_edge_case3(self):
        self.assertEqual(count_char_position("123"), 0)

    def test_edge_case4(self):
        self.assertEqual(count_char_position("aBc"), 1)

    def test_edge_case5(self):
        self.assertEqual(count_char_position("AaBbCc"), 3)

    def test_edge_case6(self):
        self.assertEqual(count_char_position("aAaBbCc"), 3)

    def test_edge_case7(self):
        self.assertEqual(count_char_position("aAaBbCcDd"), 3)

    def test_edge_case8(self):
        self.assertEqual(count_char_position("aAaBbCcDdEe"), 3)

    def test_edge_case9(self):
        self.assertEqual(count_char_position("aAaBbCcDdEeFf"), 3)

    def test_edge_case10(self):
        self.assertEqual(count_char_position("aAaBbCcDdEeFfGg"), 3)

    def test_edge_case11(self):
        self.assertEqual(count_char_position("aAaBbCcDdEeFfGgHh"), 3)

    def test_edge_case12(self):
        self.assertEqual(count_char_position("aAaBbCcDdEeFfGgHhIi"), 3)

    def test_edge_case13(self):
        self.assertEqual(count_char_position("aAaBbCcDdEeFfGgHhIiJj"), 3)

    def test_edge_case14(self):
        self.assertEqual(count_char_position("aAaBbCcDdEeFfGgHhIiJjKk"), 3)

    def test_edge_case15(self):
        self.assertEqual(count_char_position("aAaBbCcDdEeFfGgHhIiJjKkLl"), 3)

    def test_edge_case16(self):
        self.assertEqual(count_char_position("aAaBbCcDdEeFfGgHhIiJjKkLlMm"), 3)

    def test_edge_case17(self):
        self.assertEqual(count_char_position("aAaBbCcDdEeFfGgHhIiJjKkLlMmNn"), 3)

    def test_edge_case18(self):
        self.assertEqual(count_char_position("aAaBbCcDdEeFfGgHhIiJjKkLlMmNnOo"), 3)

    def test_edge_case19(self):
        self.assertEqual(count_char_position("aAaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPp"), 3)

    def test_edge_case20(self):
        self.assertEqual(count_char_position("aAaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQq"), 3)

    def test_edge_case21(self):
        self.assertEqual(count_char_position("aAaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRr"), 3)

    def test_edge_case22(self):
        self.assertEqual(count_char_position("aAaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSs"), 3)

    def test_edge_case23(self):
        self.assertEqual(count_char_position("aAaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTt"), 3)

    def test_edge_case24(self):
        self.assertEqual(count_char_position("aAaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUu"), 3)

    def test_edge_case25(self):
        self.assertEqual(count_char_position("aAaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtU