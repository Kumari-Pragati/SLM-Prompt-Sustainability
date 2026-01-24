import unittest
from mbpp_750_code import add_tuple

class TestAddTuple(unittest.TestCase):
    def test_typical_use_case(self):
        test_list = [1, 2, 3]
        test_tup = (4, 5, 6)
        result = add_tuple(test_list, test_tup)
        self.assertEqual(result, [1, 2, 3, 4, 5, 6])

    def test_empty_list(self):
        test_list = []
        test_tup = (1, 2, 3)
        result = add_tuple(test_list, test_tup)
        self.assertEqual(result, [1, 2, 3])

    def test_empty_tuple(self):
        test_list = [1, 2, 3]
        test_tup = ()
        result = add_tuple(test_list, test_tup)
        self.assertEqual(result, [1, 2, 3])

    def test_list_with_tuple(self):
        test_list = [1, 2, 3]
        test_tup = (4, 5)
        result = add_tuple(test_list, test_tup)
        self.assertEqual(result, [1, 2, 3, 4, 5])

    def test_tuple_with_list(self):
        test_list = [1, 2]
        test_tup = (3, 4, 5)
        result = add_tuple(test_list, test_tup)
        self.assertEqual(result, [1, 2, 3, 4, 5])
