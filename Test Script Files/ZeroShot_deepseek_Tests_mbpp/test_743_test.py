import unittest
from mbpp_743_code import rotate_right

class TestRotateRight(unittest.TestCase):

    def test_rotate_right(self):
        self.assertEqual(rotate_right([1, 2, 3, 4, 5], 2, 1), [4, 5, 1, 2, 3])
        self.assertEqual(rotate_right(['a', 'b', 'c', 'd', 'e'], 1, 2), ['d', 'e', 'a', 'b', 'c'])
        self.assertEqual(rotate_right([True, False, True, False, True], 3, 2), [True, False, True, False, True])
        self.assertEqual(rotate_right([], 0, 0), [])
        self.assertEqual(rotate_right([1, 2, 3, 4, 5], 5, 0), [1, 2, 3, 4, 5])
        self.assertEqual(rotate_right([1, 2, 3, 4, 5], 0, 5), [1, 2, 3, 4, 5])
        self.assertEqual(rotate_right([1, 2, 3, 4, 5], 3, 3), [1, 2, 3, 4, 5])
