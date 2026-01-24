import unittest
from mbpp_802_code import count_Rotation

class TestCountRotation(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(count_Rotation([1, 2, 3, 4, 5], 5), 1)
        self.assertEqual(count_Rotation([5, 4, 3, 2, 1], 5), 1)
        self.assertEqual(count_Rotation([1, 2, 3, 4, 5], 1), 0)

    def test_edge(self):
        self.assertEqual(count_Rotation([1, 2, 3], 3), 1)
        self.assertEqual(count_Rotation([5, 4, 3], 3), 1)
        self.assertEqual(count_Rotation([1, 2, 3, 4], 4), 1)
        self.assertEqual(count_Rotation([1, 2, 3, 4, 5], 5), 1)

    def test_edge2(self):
        self.assertEqual(count_Rotation([1, 1, 1, 1, 1], 5), 0)
        self.assertEqual(count_Rotation([5, 5, 5, 5, 5], 5), 0)

    def test_invalid(self):
        with self.assertRaises(TypeError):
            count_Rotation(None, 5)
        with self.assertRaises(TypeError):
            count_Rotation([1, 2, 3], None)
