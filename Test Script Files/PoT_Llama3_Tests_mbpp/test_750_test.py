import unittest
from mbpp_750_code import add_tuple

class TestAddTuple(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(add_tuple([1, 2, 3], (4, 5, 6)), [1, 2, 3, 4, 5, 6])

    def test_empty_list(self):
        self.assertEqual(add_tuple([], (1, 2, 3)), [1, 2, 3])

    def test_empty_tuple(self):
        self.assertEqual(add_tuple([1, 2, 3], ()), [1, 2, 3])

    def test_single_element_list(self):
        self.assertEqual(add_tuple([1], (2,)), [1, 2])

    def test_single_element_tuple(self):
        self.assertEqual(add_tuple([1, 2, 3], (4,)), [1, 2, 3, 4])

    def test_list_of_tuples(self):
        self.assertEqual(add_tuple([1, 2, 3], ((4, 5), (6, 7))), [1, 2, 3, 4, 5, 6, 7])

    def test_tuple_of_lists(self):
        self.assertEqual(add_tuple((1, 2, 3), [[4, 5], [6, 7]]), [1, 2, 3, 4, 5, 6, 7])
