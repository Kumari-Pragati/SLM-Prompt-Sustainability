import unittest
from mbpp_660_code import find_Points

class TestFindPoints(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(find_Points(1, 2, 3, 4), (1, 4))

    def test_edge_condition(self):
        self.assertEqual(find_Points(1, 1, 1, 1), (-1, -1))

    def test_boundary_condition(self):
        self.assertEqual(find_Points(1, 2, 2, 1), (-1, 2))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            find_Points("1", 2, 3, 4)
