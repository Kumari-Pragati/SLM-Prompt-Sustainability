import unittest
from mbpp_750_code import add_tuple

class TestAddTuple(unittest.TestCase):

    def test_empty_list_and_tuple(self):
        self.assertListEqual(add_tuple([], (1, 2, 3)), [1, 2, 3])

    def test_list_and_empty_tuple(self):
        self.assertListEqual(add_tuple([4, 5, 6], ()), [4, 5, 6])

    def test_list_and_tuple_with_same_elements(self):
        self.assertListEqual(add_tuple([1, 2, 3], (1, 2, 3)), [1, 2, 3, 1, 2, 3])

    def test_list_and_tuple_with_different_elements(self):
        self.assertListEqual(add_tuple([1, 2, 3], (4, 5, 6)), [1, 2, 3, 4, 5, 6])

    def test_list_and_tuple_with_mixed_types(self):
        self.assertRaises(TypeError, add_tuple, [1, 2, 3], (4, '5', 6))

    def test_list_and_tuple_with_negative_index(self):
        self.assertRaises(IndexError, add_tuple, [1, 2, 3], ((-1,),))

    def test_list_and_tuple_with_empty_list(self):
        self.assertListEqual(add_tuple([], (1, 2, 3)), [])
