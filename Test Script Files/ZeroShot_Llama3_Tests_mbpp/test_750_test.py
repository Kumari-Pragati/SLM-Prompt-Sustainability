import unittest
from mbpp_750_code import add_tuple

class TestAddTuple(unittest.TestCase):

    def test_add_tuple(self):
        test_list = [1, 2, 3]
        test_tup = (4, 5, 6)
        result = add_tuple(test_list, test_tup)
        self.assertEqual(result, [1, 2, 3, 4, 5, 6])

    def test_add_tuple_empty_list(self):
        test_list = []
        test_tup = (4, 5, 6)
        result = add_tuple(test_list, test_tup)
        self.assertEqual(result, [4, 5, 6])

    def test_add_tuple_empty_tuple(self):
        test_list = [1, 2, 3]
        test_tup = ()
        result = add_tuple(test_list, test_tup)
        self.assertEqual(result, [1, 2, 3])

    def test_add_tuple_list_and_tuple_with_duplicates(self):
        test_list = [1, 2, 2, 3]
        test_tup = (2, 4, 4)
        result = add_tuple(test_list, test_tup)
        self.assertEqual(result, [1, 2, 2, 3, 2, 4, 4])
