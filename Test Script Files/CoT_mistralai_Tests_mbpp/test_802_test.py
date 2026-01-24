import unittest
from mbpp_802_code import count_Rotation

class TestCountRotation(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_Rotation([4, 2, 3, 1], 4), 1)
        self.assertEqual(count_Rotation([1, 2, 3, 4], 4), 0)
        self.assertEqual(count_Rotation([1, 3, 5, 7], 4), 0)

    def test_edge_case_1(self):
        self.assertEqual(count_Rotation([2, 2, 2, 2], 4), 1)

    def test_edge_case_2(self):
        self.assertEqual(count_Rotation([1, 2, 2, 1], 4), 3)

    def test_edge_case_3(self):
        self.assertEqual(count_Rotation([1, 2, 3, 4, 5], 5), 0)

    def test_invalid_input_1(self):
        self.assertRaises(TypeError, count_Rotation, [1, 2, 3], 'a')

    def test_invalid_input_2(self):
        self.assertRaises(TypeError, count_Rotation, [1, 2, 3], -1)
