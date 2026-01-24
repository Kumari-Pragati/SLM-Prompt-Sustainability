import unittest
from mbpp_802_code import count_Rotation

class TestCountRotation(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_Rotation([1, 2, 3, 4, 5], 5), 1)

    def test_edge_case(self):
        self.assertEqual(count_Rotation([5, 4, 3, 2, 1], 5), 1)

    def test_edge_case2(self):
        self.assertEqual(count_Rotation([1, 2, 3, 4, 5], 1), 0)

    def test_edge_case3(self):
        self.assertEqual(count_Rotation([1, 2, 3, 4, 5], 0), 0)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            count_Rotation("hello", 5)

    def test_invalid_input2(self):
        with self.assertRaises(TypeError):
            count_Rotation([1, 2, 3], "hello")
