import unittest
from mbpp_328_code import rotate_left

class TestRotateLeft(unittest.TestCase):

    def test_rotate_left_with_valid_input(self):
        self.assertEqual(rotate_left([1, 2, 3, 4, 5], 2, 3), [3, 4, 5, 1, 2])
        self.assertEqual(rotate_left(['a', 'b', 'c', 'd', 'e'], 1, 2), ['b', 'c', 'd', 'e', 'a'])
        self.assertEqual(rotate_left([True, False, True, False, True], 3, 4), [True, False, True, False, True])

    def test_rotate_left_with_invalid_input(self):
        with self.assertRaises(IndexError):
            rotate_left([1, 2, 3, 4, 5], 6, 3)
        with self.assertRaises(IndexError):
            rotate_left([1, 2, 3, 4, 5], 2, 6)
        with self.assertRaises(IndexError):
            rotate_left([1, 2, 3, 4, 5], 6, 6)
