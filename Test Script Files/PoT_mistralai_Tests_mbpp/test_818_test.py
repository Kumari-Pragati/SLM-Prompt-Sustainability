import unittest
from mbpp_818_code import lower_ctr

class TestLowerCtr(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(lower_ctr("abcdefg"), 7)
        self.assertEqual(lower_ctr("ABCDEFG"), 7)
        self.assertEqual(lower_ctr("abc123"), 4)
        self.assertEqual(lower_ctr("123abc"), 4)

    def test_edge_case(self):
        self.assertEqual(lower_ctr("a"), 1)
        self.assertEqual(lower_ctr("z"), 1)
        self.assertEqual(lower_ctr(""), 0)
        self.assertEqual(lower_ctr("aaa"), 3)
        self.assertEqual(lower_ctr("zzz"), 3)

    def test_boundary_case(self):
        self.assertEqual(lower_ctr("a\nb"), 2)
        self.assertEqual(lower_ctr("a\n\nb"), 2)
        self.assertEqual(lower_ctr("a\n\nb\nc"), 3)
