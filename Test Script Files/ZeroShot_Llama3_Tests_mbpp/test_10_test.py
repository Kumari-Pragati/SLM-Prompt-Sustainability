import unittest
from mbpp_10_code import small_nnum

class TestSmallNnum(unittest.TestCase):

    def test_small_nnum(self):
        self.assertEqual(small_nnum([1,2,3,4,5], 3), [1,2,3])
        self.assertEqual(small_nnum([5,4,3,2,1], 3), [1,2,3])
        self.assertEqual(small_nnum([10,9,8,7,6], 2), [6,7])
        self.assertEqual(small_nnum([1,2,3,4,5], 5), [1,2,3,4,5])
        self.assertEqual(small_nnum([5,4,3,2,1], 1), [1])

    def test_small_nnum_empty_list(self):
        self.assertEqual(small_nnum([], 3), [])

    def test_small_nnum_negative_n(self):
        with self.assertRaises(ValueError):
            small_nnum([1,2,3,4,5], -3)

    def test_small_nnum_non_integer_n(self):
        with self.assertRaises(TypeError):
            small_nnum([1,2,3,4,5], 3.5)
