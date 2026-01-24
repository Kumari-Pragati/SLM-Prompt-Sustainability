import unittest
from mbpp_750_code import add_tuple

class TestAddTuple(unittest.TestCase):

    def test_add_tuple_typical_case(self):
        test_list = [1, 2, 3]
        test_tup = (4, 5)
        expected_result = [1, 2, 3, 4, 5]
        self.assertEqual(add_tuple(test_list, test_tup), expected_result)

    def test_add_tuple_empty_tuple(self):
        test_list = [1, 2, 3]
        test_tup = ()
        expected_result = [1, 2, 3]
        self.assertEqual(add_tuple(test_list, test_tup), expected_result)

    def test_add_tuple_empty_list(self):
        test_list = []
        test_tup = (4, 5)
        expected_result = [4, 5]
        self.assertEqual(add_tuple(test_list, test_tup), expected_result)

    def test_add_tuple_empty_both(self):
        test_list = []
        test_tup = ()
        expected_result = []
        self.assertEqual(add_tuple(test_list, test_tup), expected_result)
