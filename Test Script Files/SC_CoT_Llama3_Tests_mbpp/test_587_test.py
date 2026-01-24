import unittest
from mbpp_587_code import list_tuple

class TestListTuple(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(list_tuple([1, 2, 3]), (1, 2, 3))

    def test_empty_input(self):
        self.assertEqual(list_tuple([]), ())

    def test_single_element_input(self):
        self.assertEqual(list_tuple([5]), (5,))

    def test_multiple_edge_cases(self):
        self.assertEqual(list_tuple([-1, 0, 1]), (-1, 0, 1))
        self.assertEqual(list_tuple([1, 2, 3, 4, 5]), (1, 2, 3, 4, 5))
        self.assertEqual(list_tuple([-5, -4, -3, -2, -1]), (-5, -4, -3, -2, -1))

    def test_non_list_input(self):
        with self.assertRaises(TypeError):
            list_tuple("not a list")

    def test_nested_list_input(self):
        with self.assertRaises(TypeError):
            list_tuple([[1, 2], [3, 4]])
