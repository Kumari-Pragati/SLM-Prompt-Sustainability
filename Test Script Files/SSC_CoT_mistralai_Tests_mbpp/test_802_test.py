import unittest
from mbpp_802_code import count_Rotation

class TestCountRotation(unittest.TestCase):
    def test_normal_case(self):
        self.assertEqual(count_Rotation([4, 2, 3, 1], 4), 1)
        self.assertEqual(count_Rotation([1, 2, 3, 4], 4), 0)
        self.assertEqual(count_Rotation([10, 20, 30, 40], 4), 0)

    def test_edge_cases(self):
        self.assertEqual(count_Rotation([1, 2, 3], 3), 1)
        self.assertEqual(count_Rotation([1, 2, 3], 2), 0)
        self.assertEqual(count_Rotation([1, 2, 3], 1), 0)

    def test_reverse_case(self):
        self.assertEqual(count_Rotation([3, 2, 1], 3), 2)
        self.assertEqual(count_Rotation([3, 2, 1], 2), 1)
        self.assertEqual(count_Rotation([3, 2, 1], 1), 0)

    def test_single_element(self):
        self.assertEqual(count_Rotation([1], 1), 0)

    def test_invalid_input(self):
        self.assertRaises(TypeError, count_Rotation, [1, 2, 3], 'not_an_integer')
        self.assertRaises(TypeError, count_Rotation, [1, 2, 3], None)
        self.assertRaises(TypeError, count_Rotation, [1, 2, 3], [1, 2, 3])
