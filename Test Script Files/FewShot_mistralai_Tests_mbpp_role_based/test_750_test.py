import unittest
from mbpp_750_code import add_tuple

class TestAddTuple(unittest.TestCase):
    def test_add_list_and_tuple(self):
        test_list = [1, 2, 3]
        test_tup = (4, 5)
        result = add_tuple(test_list, test_tup)
        self.assertEqual(result, [1, 2, 3, 4, 5])

    def test_empty_list_and_tuple(self):
        test_list = []
        test_tup = (4, 5)
        result = add_tuple(test_list, test_tup)
        self.assertEqual(result, [4, 5])

    def test_list_with_one_element_and_tuple(self):
        test_list = [1]
        test_tup = (4, 5)
        result = add_tuple(test_list, test_tup)
        self.assertEqual(result, [1, 4, 5])

    def test_list_and_empty_tuple(self):
        test_list = [1, 2, 3]
        test_tup = ()
        result = add_tuple(test_list, test_tup)
        self.assertEqual(result, [1, 2, 3])
