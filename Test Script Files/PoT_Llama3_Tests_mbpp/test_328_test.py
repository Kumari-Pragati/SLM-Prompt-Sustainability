import unittest
from mbpp_328_code import rotate_left

class TestRotateLeft(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(rotate_left([1, 2, 3, 4, 5], 1, 3), [2, 3, 4, 5, 1])

    def test_edge_case_start(self):
        self.assertEqual(rotate_left([1, 2, 3, 4, 5], 0, 3), [1, 2, 3, 4, 5])

    def test_edge_case_end(self):
        self.assertEqual(rotate_left([1, 2, 3, 4, 5], 1, 5), [2, 3, 4, 5, 1])

    def test_edge_case_start_end(self):
        self.assertEqual(rotate_left([1, 2, 3, 4, 5], 0, 5), [1, 2, 3, 4, 5])

    def test_edge_case_invalid_input(self):
        with self.assertRaises(TypeError):
            rotate_left([1, 2, 3, 4, 5], 'a', 3)

    def test_edge_case_invalid_input2(self):
        with self.assertRaises(TypeError):
            rotate_left([1, 2, 3, 4, 5], 1, 'a')

    def test_edge_case_invalid_input3(self):
        with self.assertRaises(TypeError):
            rotate_left([1, 2, 3, 4, 5], 'a', 'b')
