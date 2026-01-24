import unittest
from mbpp_422_code import find_Average_Of_Cube

class TestFindAverageOfCube(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertAlmostEqual(find_Average_Of_Cube(5), 12.5)

    def test_edge_case_n_zero(self):
        with self.assertRaises(ZeroDivisionError):
            find_Average_Of_Cube(0)

    def test_edge_case_n_one(self):
        self.assertAlmostEqual(find_Average_Of_Cube(1), 1.0)

    def test_edge_case_n_large(self):
        self.assertAlmostEqual(find_Average_Of_Cube(100), 2500.0)

    def test_invalid_input_negative(self):
        with self.assertRaises(TypeError):
            find_Average_Of_Cube(-5)

    def test_invalid_input_non_integer(self):
        with self.assertRaises(TypeError):
            find_Average_Of_Cube(3.5)
