import unittest
from mbpp_750_code import add_tuple

class TestAddTuple(unittest.TestCase):
    def test_typical_input(self):
        test_list = [1, 2, 3]
        test_tup = (4, 5, 6)
        result = add_tuple(test_list, test_tup)
        self.assertEqual(result, [1, 2, 3, 4, 5, 6])

    def test_edge_case_empty_list(self):
        test_list = []
        test_tup = (4, 5, 6)
        result = add_tuple(test_list, test_tup)
        self.assertEqual(result, [4, 5, 6])

    def test_edge_case_empty_tuple(self):
        test_list = [1, 2, 3]
        test_tup = ()
        result = add_tuple(test_list, test_tup)
        self.assertEqual(result, [1, 2, 3])

    def test_edge_case_list_and_tuple_of_same_length(self):
        test_list = [1, 2, 3]
        test_tup = (1, 2, 3)
        result = add_tuple(test_list, test_tup)
        self.assertEqual(result, [1, 2, 3, 1, 2, 3])

    def test_edge_case_list_longer_than_tuple(self):
        test_list = [1, 2, 3, 4, 5]
        test_tup = (1, 2, 3)
        result = add_tuple(test_list, test_tup)
        self.assertEqual(result, [1, 2, 3, 4, 5])

    def test_edge_case_tuple_longer_than_list(self):
        test_list = [1, 2, 3]
        test_tup = (1, 2, 3, 4, 5)
        result = add_tuple(test_list, test_tup)
        self.assertEqual(result, [1, 2, 3, 4, 5])

    def test_invalid_input_non_iterable(self):
        test_list = [1, 2, 3]
        test_tup = 'not a tuple'
        with self.assertRaises(TypeError):
            add_tuple(test_list, test_tup)

    def test_invalid_input_non_iterable_list(self):
        test_list = [1, 2, 3]
        test_tup = 123
        with self.assertRaises(TypeError):
            add_tuple(test_list, test_tup)
