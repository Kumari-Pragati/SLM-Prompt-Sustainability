import unittest
from mbpp_847_code import lcopy

class TestLCopy(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(lcopy([1, 2, 3]), [1, 2, 3])

    def test_empty_list(self):
        self.assertEqual(lcopy([]), [])

    def test_single_element_list(self):
        self.assertEqual(lcopy([4]), [4])

    def test_list_with_negative_index(self):
        self.assertEqual(lcopy([-1, -2, -3]), [-1, -2, -3])

    def test_list_with_out_of_range_index(self):
        self.assertEqual(lcopy([0, 1, 2]), [0, 1, 2])

    def test_list_with_none(self):
        self.assertEqual(lcopy([None]), [None])

    def test_list_with_string(self):
        self.assertEqual(lcopy(["a", "b", "c"]), ["a", "b", "c"])

    def test_list_with_mixed_types(self):
        self.assertEqual(lcopy([1, "a", 3.14]), [1, "a", 3.14])
