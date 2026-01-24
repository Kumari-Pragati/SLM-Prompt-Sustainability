import unittest
from mbpp_580_code import MagicMock
from 580_code import extract_even

class TestExtractEven(unittest.TestCase):
    def test_normal_input(self):
        self.assertListEqual(extract_even((1, 2, 3, 4, 5, 6)), (2, 4, 6))
        self.assertListEqual(extract_even((1, 2, 3, (4, 5, 6), 7, 8)), (2, 4, 6))

    def test_edge_input(self):
        self.assertListEqual(extract_even((0, 2, 4)), (0, 2, 4))
        self.assertListEqual(extract_even((-1, 0, 1)), [])
        self.assertListEqual(extract_even((1, 2, 3, 4, 5, 6, 7)), (2, 4, 6))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            extract_even(123)
        with self.assertRaises(TypeError):
            extract_even([1, 2, 3])
