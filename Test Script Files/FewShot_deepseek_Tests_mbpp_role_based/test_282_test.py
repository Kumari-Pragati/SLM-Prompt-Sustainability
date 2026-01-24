import unittest
from mbpp_282_code import sub_list

class TestSubList(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(sub_list([1, 2, 3], [4, 5, 6]), [-3, -3, -3])

    def test_edge_condition(self):
        self.assertEqual(sub_list([0], [0]), [0])

    def test_boundary_condition(self):
        self.assertEqual(sub_list([1000000000], [1]), [999999999])

    def test_different_lengths(self):
        self.assertEqual(sub_list([1, 2, 3, 4], [1, 2]), [0, 0, 3])

    def test_negative_numbers(self):
        self.assertEqual(sub_list([-1, -2, -3], [-4, -5, -6]), [3, 3, 3])

    def test_zero_numbers(self):
        self.assertEqual(sub_list([0, 0, 0], [0, 0, 0]), [0, 0, 0])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            sub_list("1, 2, 3", [1, 2, 3])
        with self.assertRaises(TypeError):
            sub_list([1, 2, 3], "1, 2, 3")
        with self.assertRaises(TypeError):
            sub_list("1, 2, 3", "1, 2, 3")
