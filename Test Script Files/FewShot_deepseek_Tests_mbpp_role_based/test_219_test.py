import unittest
from mbpp_219_code import extract_min_max

class TestExtractMinMax(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(extract_min_max((1, 2, 3, 4, 5), 2), (1, 5))

    def test_edge_case(self):
        self.assertEqual(extract_min_max((1, 2, 3, 4, 5), 0), ())

    def test_boundary_case(self):
        self.assertEqual(extract_min_max((1, 2, 3, 4, 5), 5), (1, 2, 3, 4, 5))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            extract_min_max("1, 2, 3, 4, 5", 2)

        with self.assertRaises(TypeError):
            extract_min_max((1, 2, 3, 4, 5), "2")

        with self.assertRaises(ValueError):
            extract_min_max((1, 2, 3, 4, 5), 6)

        with self.assertRaises(ValueError):
            extract_min_max((1, 2, 3, 4, 5), -1)
