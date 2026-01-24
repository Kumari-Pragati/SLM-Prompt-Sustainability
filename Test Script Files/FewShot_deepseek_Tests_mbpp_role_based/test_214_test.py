import unittest
from mbpp_214_code import degree_radian

class TestDegreeRadian(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertAlmostEqual(degree_radian(1), 57.29577951308232, places=5)

    def test_boundary_condition(self):
        self.assertAlmostEqual(degree_radian(0), 0)

    def test_edge_condition(self):
        self.assertAlmostEqual(degree_radian(math.pi), 180)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            degree_radian('invalid')
