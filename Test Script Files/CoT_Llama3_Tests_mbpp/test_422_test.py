import unittest
from mbpp_422_code import find_Average_Of_Cube

class TestFindAverageOfCube(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(find_Average_Of_Cube(5), 14.583333)
        self.assertEqual(find_Average_Of_Cube(10), 24.583333)
        self.assertEqual(find_Average_Of_Cube(15), 34.583333)

    def test_edge_cases(self):
        self.assertEqual(find_Average_Of_Cube(1), 1.0)
        self.assertEqual(find_Average_Of_Cube(2), 2.0)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            find_Average_Of_Cube('a')
        with self.assertRaises(TypeError):
            find_Average_Of_Cube(None)

    def test_boundary_conditions(self):
        self.assertEqual(find_Average_Of_Cube(0), 0.0)
        self.assertEqual(find_Average_Of_Cube(-1), 0.0)
