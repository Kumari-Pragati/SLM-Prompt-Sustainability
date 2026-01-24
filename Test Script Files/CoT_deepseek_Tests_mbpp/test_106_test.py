import unittest
from mbpp_106_code import add_lists

class TestAddLists(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(add_lists([1, 2, 3], (4, 5, 6)), (4, 5, 6, 1, 2, 3))

    def test_empty_list(self):
        self.assertEqual(add_lists([], (1, 2, 3)), (1, 2, 3))

    def test_empty_tuple(self):
        self.assertEqual(add_lists([1, 2, 3], ()), ([1, 2, 3],))

    def test_mixed_types(self):
        self.assertEqual(add_lists(['a', 'b', 'c'], (1, 2, 3)), (1, 2, 3, 'a', 'b', 'c'))

    def test_large_input(self):
        test_list = list(range(1, 1001))
        test_tup = tuple(range(1001, 2001))
        self.assertEqual(add_lists(test_list, test_tup), (*test_tup, *test_list))
