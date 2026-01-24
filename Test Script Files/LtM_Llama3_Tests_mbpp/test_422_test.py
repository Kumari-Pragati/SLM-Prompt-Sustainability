import unittest
from mbpp_422_code import find_Average_Of_Cube

class TestFindAverageOfCube(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(find_Average_Of_Cube(1), 1)
        self.assertEqual(find_Average_Of_Cube(2), 8)
        self.assertEqual(find_Average_Of_Cube(3), 14.5)

    def test_edge_cases(self):
        self.assertEqual(find_Average_Of_Cube(0), 0)
        self.assertEqual(find_Average_Of_Cube(10), 285.5)
        self.assertEqual(find_Average_Of_Cube(100), 32855000.0)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            find_Average_Of_Cube('a')
        with self.assertRaises(TypeError):
            find_Average_Of_Cube(None)
