import unittest
from mbpp_586_code import split_Arr

class TestSplit_Arr(unittest.TestCase):

    def test_split_Arr_typical(self):
        self.assertEqual(split_Arr([1,2,3,4,5,6], 2, 3), [4,5,6,[1,2,3]])

    def test_split_Arr_edge1(self):
        self.assertEqual(split_Arr([1,2,3,4,5], 1, 1), [2,3,4,5,[1]])

    def test_split_Arr_edge2(self):
        self.assertEqual(split_Arr([1,2,3,4,5], 5, 5), [1,2,3,4,[5]])

    def test_split_Arr_edge3(self):
        self.assertEqual(split_Arr([1,2,3,4,5], 0, 0), [1,2,3,4,5])

    def test_split_Arr_invalid_input1(self):
        with self.assertRaises(TypeError):
            split_Arr('a', 2, 3)

    def test_split_Arr_invalid_input2(self):
        with self.assertRaises(TypeError):
            split_Arr([1,2,3,4,5], 'a', 3)

    def test_split_Arr_invalid_input3(self):
        with self.assertRaises(TypeError):
            split_Arr([1,2,3,4,5], 2, 'a')
