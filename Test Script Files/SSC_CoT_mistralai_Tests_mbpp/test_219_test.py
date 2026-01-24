import unittest
from mbpp_219_code import extract_min_max

class TestExtractMinMax(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(extract_min_max((1, 2, 3, 4, 5), 2), (1, 3))
        self.assertEqual(extract_min_max((-1, -2, -3, -4, -5), 2), (-1, -3))
        self.assertEqual(extract_min_max((0, 0, 0, 0, 0), 2), (0, 0))

    def test_edge_input(self):
        self.assertEqual(extract_min_max((1, 2, 3, 4, 5), 1), (1,))
        self.assertEqual(extract_min_max((1, 2, 3, 4, 5), 3), (3, 5))
        self.assertEqual(extract_min_max((1, 2, 3, 4, 5), 0), ())
        self.assertEqual(extract_min_max((1, 2, 3, 4, 5), 5), (1, 2, 3, 4, 5))

    def test_boundary_input(self):
        self.assertEqual(extract_min_max((-1, -1, -1, -1, -1), 0), ())
        self.assertEqual(extract_min_max((1, 1, 1, 1, 1), 4), (1, 1, 1, 1))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            extract_min_max(1.234, 2)
        with self.assertRaises(TypeError):
            extract_min_max([1, 2, 3], 'K')
