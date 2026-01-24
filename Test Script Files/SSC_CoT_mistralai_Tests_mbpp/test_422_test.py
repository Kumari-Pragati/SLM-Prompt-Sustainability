import unittest
from mbpp_422_code import find_Average_Of_Cube

class TestFindAverageOfCube(unittest.TestCase):

    def test_normal_input(self):
        self.assertAlmostEqual(find_Average_Of_Cube(3), 2.166667)
        self.assertAlmostEqual(find_Average_Of_Cube(5), 6.04375)
        self.assertAlmostEqual(find_Average_Of_Cube(10), 100.099609)

    def test_edge_and_boundary_conditions(self):
        self.assertAlmostEqual(find_Average_Of_Cube(1), 1.0)
        self.assertAlmostEqual(find_Average_Of_Cube(2), 8.0)
        self.assertAlmostEqual(find_Average_Of_Cube(1000), 123456789.0)
        self.assertAlmostEqual(find_Average_Of_Cube(0), 0.0)

    def test_negative_input(self):
        with self.assertRaises(ValueError):
            find_Average_Of_Cube(-1)
