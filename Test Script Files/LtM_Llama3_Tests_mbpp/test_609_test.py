import unittest
from mbpp_609_code import floor_Min

class TestFloorMin(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(floor_Min(2, 3, 4), 2)
        self.assertEqual(floor_Min(5, 3, 4), 4)
        self.assertEqual(floor_Min(1, 2, 3), 1)

    def test_edge(self):
        self.assertEqual(floor_Min(2, 2, 1), 1)
        self.assertEqual(floor_Min(5, 5, 5), 5)
        self.assertEqual(floor_Min(1, 1, 1), 1)

    def test_invalid(self):
        with self.assertRaises(TypeError):
            floor_Min('a', 3, 4)
        with self.assertRaises(TypeError):
            floor_Min(2, 'b', 4)
        with self.assertRaises(TypeError):
            floor_Min(2, 3, 'c')
