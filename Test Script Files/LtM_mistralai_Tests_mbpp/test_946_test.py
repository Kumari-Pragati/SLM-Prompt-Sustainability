import unittest
from mbpp_946_code import most_common_elem

class TestMostCommonElem(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(most_common_elem("abcdabcd", 1), [('a', 4)])
        self.assertEqual(most_common_elem("aabbcc", 2), [('a', 2), ('b', 2)])
        self.assertEqual(most_common_elem("aa", 1), [('a', 2)])
        self.assertEqual(most_common_elem("", 1), [])

    def test_edge_cases(self):
        self.assertEqual(most_common_elem("abcdabcd", 2), [('a', 4), ('d', 1)])
        self.assertEqual(most_common_elem("aabbcc", 3), [('a', 2), ('b', 2), ('c', 1)])
        self.assertEqual(most_common_elem("aa", 2), [('a', 2)])
        self.assertEqual(most_common_elem("", 1), [])
        self.assertEqual(most_common_elem("abcd", 3), [])

    def test_complex(self):
        self.assertEqual(most_common_elem("ababcdabab", 2), [('a', 4), ('b', 3)])
        self.assertEqual(most_common_elem("aabbccaa", 3), [('a', 3), ('b', 2), ('c', 1)])
        self.assertEqual(most_common_elem("aaabbbccc", 2), [('a', 3), ('b', 3)])
        self.assertEqual(most_common_elem("aaabbbccc", 3), [('a', 3), ('b', 3), ('c', 1)])
