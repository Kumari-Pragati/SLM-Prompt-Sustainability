import unittest
from mbpp_106_code import add_lists

class TestAddLists(unittest.TestCase):
    def test_typical_use_case(self):
        test_list = [1, 2, 3]
        test_tup = (4, 5, 6)
        expected_output = (4, 5, 6, 1, 2, 3)
        self.assertEqual(add_lists(test_list, test_tup), expected_output)

    def test_empty_list_and_tuple(self):
        test_list = []
        test_tup = ()
        expected_output = ()
        self.assertEqual(add_lists(test_list, test_tup), expected_output)

    def test_single_element_list_and_tuple(self):
        test_list = [1]
        test_tup = (2,)
        expected_output = (2, 1)
        self.assertEqual(add_lists(test_list, test_tup), expected_output)

    def test_large_list_and_tuple(self):
        test_list = list(range(1, 1001))
        test_tup = tuple(range(1001, 2001))
        expected_output = test_tup + test_list
        self.assertEqual(add_lists(test_list, test_tup), expected_output)

    def test_invalid_input(self):
        test_list = [1, 2, 3]
        test_tup = "not a tuple"
        with self.assertRaises(TypeError):
            add_lists(test_list, test_tup)
