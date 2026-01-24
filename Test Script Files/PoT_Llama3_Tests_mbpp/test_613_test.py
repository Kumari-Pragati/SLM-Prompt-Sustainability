import unittest
from mbpp_613_code import maximum_value

class TestMaximumValue(unittest.TestCase):

    def test_typical_case(self):
        test_list = [('a', [1, 2, 3]), ('b', [4, 5, 6])]
        self.assertEqual(maximum_value(test_list), [('a', 3), ('b', 6)])

    def test_edge_case(self):
        test_list = [('a', [1]), ('b', [2])]
        self.assertEqual(maximum_value(test_list), [('a', 1), ('b', 2)])

    def test_edge_case2(self):
        test_list = [('a', [1, 2]), ('b', [2, 3])]
        self.assertEqual(maximum_value(test_list), [('a', 2), ('b', 3)])

    def test_edge_case3(self):
        test_list = [('a', [1, 2, 3, 4, 5])]
        self.assertEqual(maximum_value(test_list), [('a', 5)])

    def test_edge_case4(self):
        test_list = [('a', [1, 2, 3, 4, 5, 6])]
        self.assertEqual(maximum_value(test_list), [('a', 6)])

    def test_edge_case5(self):
        test_list = [('a', [])]
        self.assertEqual(maximum_value(test_list), [('a',)])

    def test_edge_case6(self):
        test_list = [('a', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])]
        self.assertEqual(maximum_value(test_list), [('a', 10)])
