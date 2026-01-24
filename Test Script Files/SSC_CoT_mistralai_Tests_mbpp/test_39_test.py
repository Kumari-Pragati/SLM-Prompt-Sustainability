import unittest
from mbpp_39_code import Counter
from heapq import heappush, heappop, heapify

from thirtynine_code import rearange_string

class TestRearrangeString(unittest.TestCase):

    def test_normal_case(self):
        self.assertEqual(rearange_string("ababcbac"), "abcbac")
        self.assertEqual(rearange_string("aabbbcc"), "bccabba")
        self.assertEqual(rearange_string("a"), "a")
        self.assertEqual(rearange_string("aa"), "aa")
        self.assertEqual(rearange_string("aaa"), "aaa")

    def test_edge_cases(self):
        self.assertEqual(rearange_string("aabbccdd"), "bccdada")
        self.assertEqual(rearange_string("abababab"), "ababab")
        self.assertEqual(rearange_string(""), "")
        self.assertEqual(rearange_string("aabbccddaa"), "bccdadaa")
        self.assertEqual(rearange_string("aaabbbccc"), "bcccabbbaa")

    def test_boundary_conditions(self):
        self.assertEqual(rearange_string("a" * 1001), "a" * 1001)
        self.assertEqual(rearange_string("a" * 1000 + "b"), "b" + "a" * 999)
        self.assertEqual(rearange_string("a" * 1000 + "aa"), "aa" + "a" * 998)

    def test_invalid_inputs(self):
        self.assertEqual(rearange_string(123), "")
        self.assertEqual(rearange_string(None), "")
        self.assertEqual(rearange_string(""), "")
        self.assertEqual(rearange_string(" "), "")
