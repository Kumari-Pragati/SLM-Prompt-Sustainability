import unittest
from mbpp_282_code import sub_list

class TestSubList(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(sub_list([1, 2, 3], [4, 5, 6]), [-3, -3, -3])
        self.assertEqual(sub_list([1, 2, 3], [1, 2, 3]), [0, 0, 0])
        self.assertEqual(sub_list([1, 2, 3], [3, 2, 1]), [0, 0, 0])

    def test_empty_inputs(self):
        self.assertEqual(sub_list([], []), [])
        self.assertEqual(sub_list([1, 2, 3], []), [])
        self.assertEqual(sub_list([], [1, 2, 3]), [])

    def test_single_element_inputs(self):
        self.assertEqual(sub_list([1], [2]), [-1])
        self.assertEqual(sub_list([1], [1]), [0])
        self.assertEqual(sub_list([1], []), [1])

    def test_edge_cases(self):
        self.assertEqual(sub_list([1, 2, 3], [3, 2, 1]), [0, 0, 0])
        self.assertEqual(sub_list([1, 2, 3], [1, 2, 3]), [0, 0, 0])
        self.assertEqual(sub_list([1, 2, 3], [4, 5, 6]), [-3, -3, -3])

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            sub_list('a', [1, 2, 3])
        with self.assertRaises(TypeError):
            sub_list([1, 2, 3], 'a')
