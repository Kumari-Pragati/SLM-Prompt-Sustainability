import unittest
from mbpp_422_code import find_Average_Of_Cube

class TestFindAverageOfCube(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(find_Average_Of_Cube(3), 6.125000)
        self.assertEqual(find_Average_Of_Cube(5), 16.375000)
        self.assertEqual(find_Average_Of_Cube(10), 37.5)

    def test_edge_cases(self):
        self.assertEqual(find_Average_Of_Cube(1), 1.0)
        self.assertEqual(find_Average_Of_Cube(0), 0.0)
        self.assertEqual(find_Average_Of_Cube(-1), 0.0)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            find_Average_Of_Cube("a")
        with self.assertRaises(TypeError):
            find_Average_Of_Cube([1, 2, 3])
        with self.assertRaises(TypeError):
            find_Average_Of_Cube(None)

    def test_large_input(self):
        self.assertAlmostEqual(find_Average_Of_Cube(1000), 249.999999)
