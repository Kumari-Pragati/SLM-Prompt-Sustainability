import unittest
from mbpp_587_code import list_tuple

class TestListTuple(unittest.TestCase):
    def test_list_tuple_empty(self):
        self.assertEqual(list_tuple([]), ())

    def test_list_tuple_single_element(self):
        self.assertEqual(list_tuple([1]), (1,))

    def test_list_tuple_multiple_elements(self):
        self.assertEqual(list_tuple([1, 2, 3]), (1, 2, 3))

    def test_list_tuple_mixed_types(self):
        self.assertEqual(list_tuple([1, 'a', 3.14]), (1, 'a', 3.14))

    def test_list_tuple_non_list_input(self):
        with self.assertRaises(TypeError):
            list_tuple('not a list')

    def test_list_tuple_non_iterable_input(self):
        with self.assertRaises(TypeError):
            list_tuple(None)
