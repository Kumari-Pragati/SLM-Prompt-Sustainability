import unittest
from mbpp_422_code import find_Average_Of_Cube

class TestFindAverageOfCube(unittest.TestCase):

    def test_typical_cases(self):
        self.assertAlmostEqual(find_Average_Of_Cube(1), 1.0)
        self.assertAlmostEqual(find_Average_Of_Cube(2), 4.5)
        self.assertAlmostEqual(find_Average_Of_Cube(3), 9.166666666666666)

    def test_boundary_conditions(self):
        self.assertAlmostEqual(find_Average_Of_Cube(0), 0.0)
        self.assertAlmostEqual(find_Average_Of_Cube(1000), 333333.3333333333)

    def test_edge_cases(self):
        self.assertAlmostEqual(find_Average_Of_Cube(10000), 333333333.3333333)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            find_Average_Of_Cube("10")
        with self.assertRaises(ValueError):
            find_Average_Of_Cube(-10)
