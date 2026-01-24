import unittest
from mbpp_587_code import list_tuple

class TestListTuple(unittest.TestCase):
    def test_typical(self):
        self.assertEqual(list_tuple([1, 2, 3]), (1, 2, 3))

    def test_empty_list(self):
        self.assertEqual(list_tuple([]), ())

    def test_single_element(self):
        self.assertEqual(list_tuple([4]), (4,))

    def test_multiple_types(self):
        self.assertEqual(list_tuple([1, 'a', 3.5]), (1, 'a', 3.5))

    def test_list_with_duplicates(self):
        self.assertEqual(list_tuple([1, 2, 2, 3, 3, 3]), (1, 2, 2, 3, 3))

    def test_list_with_negative_numbers(self):
        self.assertEqual(list_tuple([-1, 0, 1]), (-1, 0, 1))

    def test_list_with_zero(self):
        self.assertEqual(list_tuple([0, 1, 2]), (0, 1, 2))
