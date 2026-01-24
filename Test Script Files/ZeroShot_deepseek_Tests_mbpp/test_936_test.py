import unittest
from mbpp_936_code import re_arrange_tuples

class TestRearrangeTuples(unittest.TestCase):

    def test_re_arrange_tuples(self):
        test_list = [('a', 1), ('b', 2), ('c', 3)]
        ord_list = ['b', 'a', 'c']
        self.assertEqual(re_arrange_tuples(test_list, ord_list), [('b', 2), ('a', 1), ('c', 3)])

        test_list = [('x', 10), ('y', 20), ('z', 30)]
        ord_list = ['z', 'y', 'x']
        self.assertEqual(re_arrange_tuples(test_list, ord_list), [('z', 30), ('y', 20), ('x', 10)])

        test_list = [('p', 40), ('q', 50), ('r', 60)]
        ord_list = ['p', 'q', 'r']
        self.assertEqual(re_arrange_tuples(test_list, ord_list), [('p', 40), ('q', 50), ('r', 60)])
