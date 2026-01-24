import unittest
from mbpp_422_code import find_Average_Of_Cube

class TestFindAverageOfCube(unittest.TestCase):

    def test_typical_cases(self):
        self.assertAlmostEqual(find_Average_Of_Cube(1), 1.0, places=6)
        self.assertAlmostEqual(find_Average_Of_Cube(2), 4.25, places=6)
        self.assertAlmostEqual(find_Average_Of_Cube(3), 9.6, places=6)

    def test_edge_cases(self):
        self.assertAlmostEqual(find_Average_Of_Cube(0), 0.0, places=6)
        self.assertAlmostEqual(find_Average_Of_Cube(100), 34019.75, places=6)

    def test_negative_numbers(self):
        with self.assertRaises(ValueError):
            find_Average_Of_Cube(-1)

    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            find_Average_Of_Cube(1.5)
