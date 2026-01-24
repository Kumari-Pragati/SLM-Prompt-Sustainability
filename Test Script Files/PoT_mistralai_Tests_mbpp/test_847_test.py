import unittest
from mbpp_847_code import lcopy

class TestLcopy(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(lcopy([1, 2, 3]), [1, 2, 3])

    def test_empty_list(self):
        self.assertEqual(lcopy([]), [])

    def test_single_element(self):
        self.assertEqual(lcopy([4]), [4])

    def test_negative_index(self):
        self.assertEqual(lcopy([-1, -2, -3]), [-1, -2, -3])

    def test_slice_beyond_end(self):
        self.assertEqual(lcopy([0, 1, 2]), [0, 1, 2])

    def test_list_with_none(self):
        self.assertEqual(lcopy([None]), [None])
