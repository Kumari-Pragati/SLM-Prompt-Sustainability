import unittest
from mbpp_106_code import add_lists

class TestAddLists(unittest.TestCase):

    def test_typical_case(self):
        test_list = [1, 2, 3]
        test_tup = (4, 5, 6)
        expected_result = (4, 5, 6, 1, 2, 3)
        self.assertEqual(add_lists(test_list, test_tup), expected_result)

    def test_empty_list(self):
        test_list = []
        test_tup = (4, 5, 6)
        expected_result = (4, 5, 6)
        self.assertEqual(add_lists(test_list, test_tup), expected_result)

    def test_empty_tuple(self):
        test_list = [1, 2, 3]
        test_tup = ()
        expected_result = (1, 2, 3)
        self.assertEqual(add_lists(test_list, test_tup), expected_result)

    def test_empty_both(self):
        test_list = []
        test_tup = ()
        expected_result = ()
        self.assertEqual(add_lists(test_list, test_tup), expected_result)

    def test_large_input(self):
        test_list = list(range(1, 1001))
        test_tup = tuple(range(1001, 2001))
        expected_result = test_tup + test_list
        self.assertEqual(add_lists(test_list, test_tup), expected_result)
