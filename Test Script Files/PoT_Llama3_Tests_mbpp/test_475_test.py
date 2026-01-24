import unittest
from mbpp_475_code import sort_counter

class TestSortCounter(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(sort_counter({'a': 3, 'b': 2, 'c': 1}), [('c', 1), ('b', 2), ('a', 3)])

    def test_edge_case(self):
        self.assertEqual(sort_counter({'a': 1}), [('a', 1)])

    def test_edge_case2(self):
        self.assertEqual(sort_counter({'a': 1, 'b': 1}), [('a', 1), ('b', 1)])

    def test_edge_case3(self):
        self.assertEqual(sort_counter({}), [])

    def test_edge_case4(self):
        self.assertEqual(sort_counter({'a': 1, 'b': 2, 'c': 3}), [('c', 3), ('b', 2), ('a', 1)])

    def test_edge_case5(self):
        self.assertEqual(sort_counter({'a': 1, 'b': 2, 'c': 2}), [('c', 2), ('b', 2), ('a', 1)])

    def test_edge_case6(self):
        self.assertEqual(sort_counter({'a': 1, 'b': 1, 'c': 1}), [('a', 1), ('b', 1), ('c', 1)])
