import unittest
from mbpp_14_code import find_Volume

class TestFindVolume(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertAlmostEqual(find_Volume(1, 2, 3), 1.5)
        self.assertAlmostEqual(find_Volume(4, 5, 6), 120.0)

    def test_boundary_conditions(self):
        self.assertEqual(find_Volume(0, 0, 0), 0)
        self.assertEqual(find_Volume(1, 1, 1), 0.5)
        self.assertAlmostEqual(find_Volume(100, 100, 100), 50000000.0)

    def test_edge_cases(self):
        self.assertAlmostEqual(find_Volume(1.5, 2.5, 3.5), 6.1875)
        self.assertAlmostEqual(find_Volume(0.5, 0.5, 0.5), 0.125)
