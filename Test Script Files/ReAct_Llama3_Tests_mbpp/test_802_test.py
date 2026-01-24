import unittest
from mbpp_802_code import count_Rotation

class TestCountRotation(unittest.TestCase):

    def test_typical_case(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(count_Rotation(arr, len(arr)), 4)

    def test_edge_case(self):
        arr = [5, 4, 3, 2, 1]
        self.assertEqual(count_Rotation(arr, len(arr)), 1)

    def test_edge_case2(self):
        arr = [1, 1, 1, 1, 1]
        self.assertEqual(count_Rotation(arr, len(arr)), 0)

    def test_edge_case3(self):
        arr = [1]
        self.assertEqual(count_Rotation(arr, len(arr)), 0)

    def test_edge_case4(self):
        arr = []
        with self.assertRaises(IndexError):
            count_Rotation(arr, len(arr))

    def test_edge_case5(self):
        arr = [1, 2]
        self.assertEqual(count_Rotation(arr, len(arr)), 1)
