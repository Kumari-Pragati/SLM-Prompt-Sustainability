import unittest
from mbpp_946_code import most_common_elem

class TestMostCommonElem(unittest.TestCase):
    def test_normal(self):
        self.assertListEqual(most_common_elem("aaabbc", 2), [('a', 3)])
        self.assertListEqual(most_common_elem("abcdefg", 3), [('a', 1), ('b', 1), ('c', 1)])

    def test_edge_cases(self):
        self.assertListEqual(most_common_elem("", 1), [])
        self.assertListEqual(most_common_elem("a", 1), [('a', 1)])
        self.assertListEqual(most_common_elem("aaa", 1), [('a', 3)])
        self.assertListEqual(most_common_elem("aaaa", 2), [('a', 4)])

    def test_boundary(self):
        self.assertListEqual(most_common_elem("aabbcc", 3), [('a', 2), ('b', 2)])
        self.assertListEqual(most_common_elem("aabbcc", 4), [('a', 2), ('b', 2), ('c', 1)])

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, most_common_elem, 1, "a")
        self.assertRaises(TypeError, most_common_elem, "a", 0)
        self.assertRaises(TypeError, most_common_elem, [], "a")
