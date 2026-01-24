import unittest
from mbpp_14_code import find_Volume

class TestFindVolume(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertAlmostEqual(find_Volume(10, 20, 30), 3000.0)

    def test_boundary_conditions(self):
        self.assertAlmostEqual(find_Volume(0, 0, 0), 0.0)
        self.assertAlmostEqual(find_Volume(1, 1, 1), 0.5)

    def test_edge_conditions(self):
        self.assertAlmostEqual(find_Volume(1000000000, 1000000000, 1000000000), 1000000000*1000000000*1000000000/2)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            find_Volume("10", 20, 30)
        with self.assertRaises(TypeError):
            find_Volume(10, "20", 30)
        with self.assertRaises(TypeError):
            find_Volume(10, 20, "30")
        with self.assertRaises(TypeError):
            find_Volume("10", "20", "30")
