import unittest
from mbpp_738_code import geometric_sum

class TestGeometricSum(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertAlmostEqual(geometric_sum(3), 1.75, places=2)

    def test_boundary_condition(self):
        self.assertEqual(geometric_sum(0), 1)

    def test_negative_number(self):
        self.assertEqual(geometric_sum(-1), 0)

    def test_large_number(self):
        self.assertAlmostEqual(geometric_sum(10), 1.83928673718, places=2)
