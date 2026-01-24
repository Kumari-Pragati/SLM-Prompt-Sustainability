import unittest
from mbpp_587_code import list_tuple

class TestListTuple(unittest.TestCase):
    def test_simple_list(self):
        self.assertEqual(list_tuple([1, 2, 3]), (1, 2, 3))

    def test_empty_list(self):
        self.assertEqual(list_tuple([]), ())

    def test_single_element_list(self):
        self.assertEqual(list_tuple([4]), (4,))

    def test_large_list(self):
        self.assertEqual(list_tuple(list(range(1000))), tuple(range(1000)))

    def test_negative_numbers(self):
        self.assertEqual(list_tuple([-1, -2, -3]), (-1, -2, -3))

    def test_mixed_numbers(self):
        self.assertEqual(list_tuple([0, 1, -1]), (0, 1, -1))
