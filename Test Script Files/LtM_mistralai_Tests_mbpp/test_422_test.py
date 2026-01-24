import unittest
from mbpp_422_code import find_Average_Of_Cube

class TestFindAverageOfCube(unittest.TestCase):

    def test_simple_input(self):
        self.assertAlmostEqual(find_Average_Of_Cube(3), 2.166667)
        self.assertAlmostEqual(find_Average_Of_Cube(4), 6.25)
        self.assertAlmostEqual(find_Average_Of_Cube(5), 12.5)

    def test_edge_and_boundary_conditions(self):
        self.assertAlmostEqual(find_Average_Of_Cube(1), 1.0)
        self.assertAlmostEqual(find_Average_Of_Cube(100), 1000000.0)
        self.assertAlmostEqual(find_Average_Of_Cube(0), 0.0)
