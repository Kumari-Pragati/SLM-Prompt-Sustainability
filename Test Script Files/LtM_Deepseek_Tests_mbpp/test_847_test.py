import unittest
from mbpp_847_code import lcopy

class TestLcopy(unittest.TestCase):
    def test_simple_list(self):
        self.assertEqual(lcopy([1, 2, 3]), [1, 2, 3])

    def test_empty_list(self):
        self.assertEqual(lcopy([]), [])

    def test_list_with_duplicates(self):
        self.assertEqual(lcopy([1, 2, 2]), [1, 2, 2])

    def test_list_with_negative_numbers(self):
        self.assertEqual(lcopy([-1, -2, -3]), [-1, -2, -3])

    def test_list_with_mixed_numbers(self):
        self.assertEqual(lcopy([1, -2, 3]), [1, -2, 3])

    def test_list_with_large_numbers(self):
        self.assertEqual(lcopy([1000, 2000, 3000]), [1000, 2000, 3000])
