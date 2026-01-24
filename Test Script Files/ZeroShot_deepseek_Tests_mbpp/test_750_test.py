import unittest
from mbpp_750_code import add_tuple

class TestAddTuple(unittest.TestCase):

    def test_add_tuple_with_empty_list_and_tuple(self):
        test_list = []
        test_tup = ()
        self.assertEqual(add_tuple(test_list, test_tup), [])

    def test_add_tuple_with_non_empty_list_and_empty_tuple(self):
        test_list = [1, 2, 3]
        test_tup = ()
        self.assertEqual(add_tuple(test_list, test_tup), [1, 2, 3])

    def test_add_tuple_with_empty_list_and_non_empty_tuple(self):
        test_list = []
        test_tup = (1, 2, 3)
        self.assertEqual(add_tuple(test_list, test_tup), [1, 2, 3])

    def test_add_tuple_with_non_empty_list_and_non_empty_tuple(self):
        test_list = [1, 2, 3]
        test_tup = (4, 5, 6)
        self.assertEqual(add_tuple(test_list, test_tup), [1, 2, 3, 4, 5, 6])
