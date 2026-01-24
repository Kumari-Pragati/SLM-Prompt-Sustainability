import unittest
from mbpp_181_code import common_prefix

class TestCommonPrefix(unittest.TestCase):
    def test_common_prefix_typical(self):
        self.assertEqual(common_prefix(["abc", "abcd", "abce"], 3), "abc")

    def test_common_prefix_edge1(self):
        self.assertEqual(common_prefix(["", "abc", "abcd"], 3), "")

    def test_common_prefix_edge2(self):
        self.assertEqual(common_prefix(["abc", "abcd", ""], 3), "abc")

    def test_common_prefix_edge3(self):
        self.assertEqual(common_prefix(["", "", ""], 3), "")

    def test_common_prefix_edge4(self):
        self.assertEqual(common_prefix(["abc", "abcd", "abcde"], 3), "abc")

    def test_common_prefix_edge5(self):
        self.assertEqual(common_prefix(["", "abc", "abcde"], 3), "")

    def test_common_prefix_edge6(self):
        self.assertEqual(common_prefix(["abc", "", "abcde"], 3), "abc")

    def test_common_prefix_edge7(self):
        self.assertEqual(common_prefix(["", "", "abcde"], 3), "")

    def test_common_prefix_edge8(self):
        self.assertEqual(common_prefix(["", "abc", "abcde"], 3), "")

    def test_common_prefix_edge9(self):
        self.assertEqual(common_prefix(["abc", "abc", "abcde"], 3), "abc")

    def test_common_prefix_edge10(self):
        self.assertEqual(common_prefix(["", "abc", "abcde", "abc"], 4), "abc")

    def test_common_prefix_edge11(self):
        self.assertEqual(common_prefix(["abc", "abc", "abcde", "abc"], 4), "abc")

    def test_common_prefix_edge12(self):
        self.assertEqual(common_prefix(["", "abc", "abcde", "abc"], 4), "")
