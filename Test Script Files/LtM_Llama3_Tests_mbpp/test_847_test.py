import unittest
from mbpp_847_code import lcopy

class TestLcopy(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(lcopy([]), [])

    def test_single_element_list(self):
        self.assertEqual(lcopy([1]), [1])

    def test_multiple_elements_list(self):
        self.assertEqual(lcopy([1, 2, 3]), [1, 2, 3])

    def test_list_with_duplicates(self):
        self.assertEqual(lcopy([1, 2, 2, 3]), [1, 2, 2, 3])

    def test_list_with_negative_numbers(self):
        self.assertEqual(lcopy([-1, 0, 1]), [-1, 0, 1])

    def test_list_with_zero(self):
        self.assertEqual(lcopy([0, 1, 2]), [0, 1, 2])

    def test_list_with_max_int(self):
        self.assertEqual(lcopy([2147483647, 1, 2]), [2147483647, 1, 2])

    def test_list_with_min_int(self):
        self.assertEqual(lcopy([-2147483648, 1, 2]), [-2147483648, 1, 2])
