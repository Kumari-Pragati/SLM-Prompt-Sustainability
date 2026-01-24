import unittest
from mbpp_609_code import floor_Min

class TestFloorMin(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(floor_Min(10, 3, 2), 6)

    def test_boundary_case(self):
        self.assertEqual(floor_Min(10, 1, 0), 10)

    def test_edge_case(self):
        self.assertEqual(floor_Min(10, 2, 1), 10)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            floor_Min("10", 3, 2)
