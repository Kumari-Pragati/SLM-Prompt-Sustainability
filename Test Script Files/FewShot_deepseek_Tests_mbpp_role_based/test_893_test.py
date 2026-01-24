import unittest
from mbpp_893_code import Extract

class TestExtract(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(Extract([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [3, 6, 9])

    def test_edge_case(self):
        self.assertEqual(Extract([[]]), [])

    def test_boundary_case(self):
        self.assertEqual(Extract([[1]]), [1])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            Extract("not a list")
