import unittest
from mbpp_422_code import find_Average_Of_Cube

class TestFindAverageOfCube(unittest.TestCase):
    def test_typical_case(self):
        self.assertAlmostEqual(find_Average_Of_Cube(3), 2.166667)
        self.assertAlmostEqual(find_Average_Of_Cube(4), 3.333333)
        self.assertAlmostEqual(find_Average_Of_Cube(5), 4.333333)

    def test_edge_case(self):
        self.assertAlmostEqual(find_Average_Of_Cube(1), 1.0)
        self.assertAlmostEqual(find_Average_Of_Cube(2), 2.0)

    def test_boundary_case(self):
        self.assertAlmostEqual(find_Average_Of_Cube(0), 0.0)
        self.assertAlmostEqual(find_Average_Of_Cube(6), 5.333333)
