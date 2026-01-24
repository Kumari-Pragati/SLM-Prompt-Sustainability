import unittest
from mbpp_750_code import add_tuple

class TestAddTuple(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(add_tuple([], (1, 2, 3)), [1, 2, 3])

    def test_single_list_element(self):
        self.assertEqual(add_tuple([4], (1, 2, 3)), [4, 1, 2, 3])

    def test_multiple_list_elements(self):
        self.assertEqual(add_tuple([4, 5], (1, 2, 3)), [4, 5, 1, 2, 3])

    def test_single_tuple_element(self):
        self.assertEqual(add_tuple([], (4,)), [4])

    def test_multiple_tuple_elements(self):
        self.assertEqual(add_tuple([4, 5], (1, 2, 3, 6, 7)), [4, 5, 1, 2, 3, 6, 7])
