import unittest
from mbpp_181_code import common_prefix

class TestCommonPrefix(unittest.TestCase):

    def test_common_prefix_typical(self):
        self.assertEqual(common_prefix(["abc", "abcd", "abce"], 3), "abc")

    def test_common_prefix_edge(self):
        self.assertEqual(common_prefix(["", "a"], 2), "")

    def test_common_prefix_edge2(self):
        self.assertEqual(common_prefix(["a", "b"], 2), "")

    def test_common_prefix_edge3(self):
        self.assertEqual(common_prefix(["a", "abc"], 2), "a")

    def test_common_prefix_edge4(self):
        self.assertEqual(common_prefix(["a", "abc", "abcd"], 3), "abc")

    def test_common_prefix_edge5(self):
        self.assertEqual(common_prefix(["a", "abc", "abcd", "abcde"], 4), "abcd")

    def test_common_prefix_edge6(self):
        self.assertEqual(common_prefix(["a", "abc", "abcd", "abcde", "abcdef"], 5), "abcde")

    def test_common_prefix_edge7(self):
        self.assertEqual(common_prefix(["a", "abc", "abcd", "abcde", "abcdef", "abcdefg"], 6, "abcdefg"), "abcdefg")

    def test_common_prefix_edge8(self):
        self.assertEqual(common_prefix(["a", "abc", "abcd", "abcde", "abcdef", "abcdefg", "abcdefh"], 7, "abcdefh"), "abcdefh")

    def test_common_prefix_edge9(self):
        self.assertEqual(common_prefix(["a", "abc", "abcd", "abcde", "abcdef", "abcdefg", "abcdefh", "abcg"], 8, "abcg"), "abcg")

    def test_common_prefix_edge10(self):
        self.assertEqual(common_prefix(["a", "abc", "abcd", "abcde", "abcdef", "abcdefg", "abcdefh", "abcg", "abcdefgh"], 9, "abcdefgh"), "abcdefgh")

    def test_common_prefix_edge11(self):
        self.assertEqual(common_prefix(["a", "abc", "abcd", "abcde", "abcdef", "abcdefg", "abcdefh", "abcg", "abcdefgh", "abcdefghi"], 10, "abcdefghi"), "abcdefghi")

    def test_common_prefix_edge12(self):
        self.assertEqual(common_prefix(["a", "abc", "abcd", "abcde", "abcdef", "abcdefg", "abcdefh", "abcg", "abcdefgh", "abcdefghi", "abcdefghj"], 11, "abcdefghj"), "abcdefghj")

    def test_common_prefix_edge13(self):
        self.assertEqual(common_prefix(["a", "abc", "abcd", "abcde", "abcdef", "abcdefg", "abcdefh", "abcg", "abcdefgh", "abcdefghi", "abcdefghj", "abcdefghk"], 12, "abcdefghk"), "abcdefghk")

    def test_common_prefix_edge14(self):
        self.assertEqual(common_prefix(["a", "abc", "abcd", "abcde", "abcdef", "abcdefg", "abcdefh", "abcg", "abcdefgh", "abcdefghi", "abcdefghj", "abcdefghk", "abcdefghl"], 13, "abcdefghl"), "abcdefghl")

    def test_common_prefix_edge15(self):
        self.assertEqual(common_prefix(["a", "abc", "abcd", "abcde", "abcdef", "abcdefg", "abcdefh", "abcg", "abcdefgh", "abcdefghi", "abcdefghj", "abcdefghk", "abcdefghl", "abc"], 14, "abc"), "abc")

    def test_common_prefix_edge16(self):
        self.assertEqual(common_prefix(["a", "abc", "abcd", "abcde", "abcdef", "abcdefg", "abcdefh", "abcg", "abcdefgh", "abcdefghi", "abcdefghj", "abcdefghk", "abcdefghl", "abc", "abcd"], 15, "abcd"), "abcd")

    def test_common_prefix_edge17(self):
        self.assertEqual(common_prefix(["a", "abc", "abcd", "abcde", "abcdef", "abcdefg", "abcdefh", "abcg", "abcdefgh", "abcdefghi", "abcdefghj", "abcdefghk", "abcdefghl", "abc", "abcd", "abcde"], 16, "abcde"), "abcde")

    def test_common_prefix_edge18(self):
        self.assertEqual(common_prefix(["a", "abc", "abcd", "abcde", "abcdef", "abcdefg", "abcdefh", "abcg", "abcdefgh", "abcdefghi", "abcdefghj", "abcdefghk", "abcdefghl", "abc", "abcd", "abcde", "abcdef"], 17, "abcdef"), "abcdef")

    def test_common_prefix_edge19(self):
        self.assertEqual(common_prefix(["a", "abc", "abcd", "abcde