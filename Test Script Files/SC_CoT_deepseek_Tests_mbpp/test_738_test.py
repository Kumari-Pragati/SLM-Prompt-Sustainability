import unittest
from mbpp_738_code import geometric_sum

class TestGeometricSum(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(geometric_sum(3), 1.9375)

    def test_boundary_case(self):
        self.assertAlmostEqual(geometric_sum(0), 1.0)

    def test_edge_case(self):
        self.assertAlmostEqual(geometric_sum(1), 1.5)

    def test_negative_case(self):
        self.assertEqual(geometric_sum(-1), 0)

    def test_large_case(self):
        self.assertAlmostEqual(geometric_sum(10), 1.6437238418572456)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            geometric_sum("abc")
