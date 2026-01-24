import unittest
from mbpp_660_code import find_Points

class TestFindPoints(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(find_Points(1, 5, 3, 7), (-3, 7))

    def test_edge_cases(self):
        self.assertEqual(find_Points(1, 1, 3, 3), (-1, 3))
        self.assertEqual(find_Points(1, 5, 5, 5), (-1, 5))

    def test_boundary_cases(self):
        self.assertEqual(find_Points(1, 5, 5, 7), (1, 7))
        self.assertEqual(find_Points(3, 7, 1, 5), (1, 5))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            find_Points('a', 5, 3, 7)
        with self.assertRaises(TypeError):
            find_Points(1, 5, 'a', 7)
        with self.assertRaises(TypeError):
            find_Points('a', 'b', 3, 7)
