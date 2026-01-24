import unittest
from mbpp_968_code import floor_Max

class TestFloorMax(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(floor_Max(1, 2, 3), 1)
        self.assertEqual(floor_Max(2, 3, 4), 2)
        self.assertEqual(floor_Max(3, 4, 5), 3)

    def test_edge(self):
        self.assertEqual(floor_Max(1, 1, 1), 0)
        self.assertEqual(floor_Max(2, 2, 2), 1)
        self.assertEqual(floor_Max(3, 3, 3), 2)

    def test_max(self):
        self.assertEqual(floor_Max(10, 10, 100), 10)
        self.assertEqual(floor_Max(20, 20, 200), 20)
        self.assertEqual(floor_Max(30, 30, 300), 30)

    def test_min(self):
        self.assertEqual(floor_Max(1, 1, 1), 0)
        self.assertEqual(floor_Max(2, 2, 2), 1)
        self.assertEqual(floor_Max(3, 3, 3), 2)

    def test_invalid(self):
        with self.assertRaises(TypeError):
            floor_Max('a', 2, 3)
        with self.assertRaises(TypeError):
            floor_Max(1, 'b', 3)
        with self.assertRaises(TypeError):
            floor_Max(1, 2, 'c')
