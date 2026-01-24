import unittest
from mbpp_422_code import find_Average_Of_Cube

class TestFindAverageOfCube(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertAlmostEqual(find_Average_Of_Cube(1), 1.0)
        self.assertAlmostEqual(find_Average_Of_Cube(2), 4.5)
        self.assertAlmostEqual(find_Average_Of_Cube(3), 9.6)

    def test_edge_conditions(self):
        self.assertAlmostEqual(find_Average_Of_Cube(0), 0.0)
        self.assertAlmostEqual(find_Average_Of_Cube(100), 334350.6)

    def test_complex_cases(self):
        self.assertAlmostEqual(find_Average_Of_Cube(1000), 451666667.0)
