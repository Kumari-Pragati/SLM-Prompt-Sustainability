import unittest
from mbpp_936_code import re_arrange_tuples

class TestReArrangeTuples(unittest.TestCase):

    def test_empty_lists(self):
        self.assertListEqual(re_arrange_tuples([], []), [])
        self.assertListEqual(re_arrange_tuples([], [1]), [(1, None)])
        self.assertListEqual(re_arrange_tuples([], [1, 2]), [(1, None), (2, None)])

    def test_single_element_lists(self):
        self.assertListEqual(re_arrange_tuples([(1, 'a')], [1]), [(1, 'a')])
        self.assertListEqual(re_arrange_tuples([(1, 'a')], [2]), [])

    def test_multiple_elements_lists(self):
        self.assertListEqual(re_arrange_tuples([(1, 'a'), (2, 'b'), (3, 'c')], [1, 2, 3]),
                             [(1, 'a'), (2, 'b')])
        self.assertListEqual(re_arrange_tuples([(1, 'a'), (2, 'b'), (3, 'c')], [1, 3]),
                             [(1, 'a'), (3, 'c')])
        self.assertListEqual(re_arrange_tuples([(1, 'a'), (2, 'b'), (3, 'c')], [2, 1]),
                             [(2, 'b'), (1, 'a')])
        self.assertListEqual(re_arrange_tuples([(1, 'a'), (2, 'b'), (3, 'c')], [4]), [])
