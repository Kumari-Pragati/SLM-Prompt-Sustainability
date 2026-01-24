import unittest
from mbpp_743_code import rotate_right

class TestRotateRight(unittest.TestCase):

    def test_typical(self):
        self.assertEqual(rotate_right([1,2,3,4,5],2,1), [4,5,1,2,3])

    def test_edge1(self):
        self.assertEqual(rotate_right([1,2,3,4,5],5,0), [1,2,3,4,5])

    def test_edge2(self):
        self.assertEqual(rotate_right([1,2,3,4,5],0,0), [1,2,3,4,5])

    def test_edge3(self):
        self.assertEqual(rotate_right([1,2,3,4,5],5,5), [1,2,3,4,5])

    def test_invalid_input1(self):
        with self.assertRaises(TypeError):
            rotate_right("abc",2,1)

    def test_invalid_input2(self):
        with self.assertRaises(TypeError):
            rotate_right([1,2,3,4,5], "abc", 1)

    def test_invalid_input3(self):
        with self.assertRaises(TypeError):
            rotate_right([1,2,3,4,5], 2, "abc")
