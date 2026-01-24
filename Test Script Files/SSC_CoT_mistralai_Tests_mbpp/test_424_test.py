import unittest
from mbpp_424_code import extract_rear

class TestExtractRear(unittest.TestCase):

    def test_normal_input(self):
        self.assertListEqual(extract_rear(([1, 2, 3], [4, 5, 6])), [3, 6])
        self.assertListEqual(extract_rear(([7, 8, 9], [], [11, 12, 13])), [9, 13])

    def test_edge_input(self):
        self.assertListEqual(extract_rear(([1], [2])), [1, 2])
        self.assertListEqual(extract_rear(([], [2])), [2])
        self.assertListEqual(extract_rear(([1], [2, 3])), [3])

    def test_boundary_input(self):
        self.assertListEqual(extract_rear(([1] * 1000, [2] * 1000)), [1000, 2000])
        self.assertListEqual(extract_rear(([1] * 1000, [2] * 1000, [3] * 1000)), [3000, 2000, 1000])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            extract_rear(123)
        with self.assertRaises(TypeError):
            extract_rear('abc')
