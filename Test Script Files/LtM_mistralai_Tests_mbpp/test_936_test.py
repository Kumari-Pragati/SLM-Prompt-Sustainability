import unittest
from mbpp_936_code import re_arrange_tuples

class TestReArrangeTuples(unittest.TestCase):

    def test_simple_input(self):
        self.assertListEqual(re_arrange_tuples([(1, 'a'), (2, 'b'), (3, 'c')], [2, 1, 3]), [(2, 'b'), (1, 'a'), (3, 'c')])

    def test_ord_list_reverse(self):
        self.assertListEqual(re_arrange_tuples([(1, 'a'), (2, 'b'), (3, 'c')], [3, 2, 1]), [(3, 'c'), (2, 'b'), (1, 'a')])

    def test_ord_list_duplicates(self):
        self.assertListEqual(re_arrange_tuples([(1, 'a'), (2, 'b'), (3, 'c')], [1, 2, 2, 3]), [(1, 'a'), (2, 'b'), (3, 'c')])

    def test_test_list_empty(self):
        self.assertListEqual(re_arrange_tuples([], [1, 2, 3]), [])

    def test_ord_list_empty(self):
        self.assertListEqual(re_arrange_tuples([(1, 'a'), (2, 'b'), (3, 'c')], []), [])

    def test_test_list_single(self):
        self.assertListEqual(re_arrange_tuples([(1, 'a')], [1]), [(1, 'a')])

    def test_ord_list_not_in_test_list(self):
        self.assertListEqual(re_arrange_tuples([(1, 'a'), (2, 'b')], [3]), [])
