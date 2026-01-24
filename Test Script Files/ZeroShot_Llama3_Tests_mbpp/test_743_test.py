import unittest
from mbpp_743_code import rotate_right

class TestRotateRight(unittest.TestCase):

    def test_rotate_right(self):
        self.assertEqual(rotate_right([1,2,3,4,5],2,1), [4,5,1,2,3])
        self.assertEqual(rotate_right([1,2,3,4,5],5,1), [1,2,3,4,5])
        self.assertEqual(rotate_right([1,2,3,4,5],0,1), [1,2,3,4,5])
        self.assertEqual(rotate_right([1,2,3,4,5],3,2), [3,4,5,1,2])
        self.assertEqual(rotate_right([1,2,3,4,5],4,3), [4,5,1,2,3])

    def test_rotate_right_invalid_input(self):
        with self.assertRaises(TypeError):
            rotate_right([1,2,3,4,5], 'a', 1)
        with self.assertRaises(TypeError):
            rotate_right([1,2,3,4,5], 1, 'a')
        with self.assertRaises(TypeError):
            rotate_right([1,2,3,4,5], 'a', 'b')
