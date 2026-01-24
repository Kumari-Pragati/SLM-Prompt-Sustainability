import unittest
from mbpp_422_code import find_Average_Of_Cube

class TestFindAverageOfCube(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertAlmostEqual(find_Average_Of_Cube(5), 225.0/5, places=6)

    def test_edge_condition(self):
        self.assertEqual(find_Average_Of_Cube(1), 1)

    def test_boundary_condition(self):
        self.assertEqual(find_Average_Of_Cube(0), 0)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            find_Average_Of_Cube('5')
