import unittest
from mbpp_576_code import is_Sub_Array

class TestIsSubArray(unittest.TestCase):
    def test_simple_valid(self):
        self.assertTrue(is_Sub_Array([1, 2, 3], [1, 2], 3, 2))

    def test_empty_array(self):
        self.assertFalse(is_Sub_Array([1, 2, 3], [], 3, 0))

    def test_empty_subarray(self):
        self.assertTrue(is_Sub_Array([1, 2, 3], [], 3, 0))

    def test_subarray_at_end(self):
        self.assertTrue(is_Sub_Array([1, 2, 3, 4, 5], [4, 5], 5, 2))

    def test_subarray_at_start(self):
        self.assertTrue(is_Sub_Array([1, 2, 3, 4, 5], [1, 2], 5, 2))

    def test_subarray_in_middle(self):
        self.assertTrue(is_Sub_Array([1, 2, 3, 4, 5, 6], [3, 4], 6, 2))

    def test_subarray_not_found(self):
        self.assertFalse(is_Sub_Array([1, 2, 3, 4, 5], [6, 7], 5, 2))

    def test_subarray_longer_than_main(self):
        self.assertFalse(is_Sub_Array([1, 2, 3], [1, 2, 3, 4], 3, 4))

    def test_subarray_shorter_than_main(self):
        self.assertTrue(is_Sub_Array([1, 2, 3, 4, 5], [1, 2], 5, 2))
