import unittest
from mbpp_328_code import rotate_left

class TestRotateLeft(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(rotate_left([1,2,3,4,5], 1, 3), [2,3,4,5,1])

    def test_edge_case1(self):
        self.assertEqual(rotate_left([1,2,3,4,5], 0, 5), [1,2,3,4,5])

    def test_edge_case2(self):
        self.assertEqual(rotate_left([1,2,3,4,5], 4, 5), [1,2,3,4,5])

    def test_edge_case3(self):
        self.assertEqual(rotate_left([1,2,3,4,5], 5, 5), [1,2,3,4,5])

    def test_edge_case4(self):
        self.assertEqual(rotate_left([1,2,3,4,5], 0, 0), [1,2,3,4,5])

    def test_invalid_input1(self):
        with self.assertRaises(TypeError):
            rotate_left('abc', 1, 2)

    def test_invalid_input2(self):
        with self.assertRaises(TypeError):
            rotate_left([1,2,3], 'a', 2)

    def test_invalid_input3(self):
        with self.assertRaises(TypeError):
            rotate_left([1,2,3], 1, 'a')
