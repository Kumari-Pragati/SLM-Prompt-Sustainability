import unittest
from mbpp_422_code import find_Average_Of_Cube

class TestFindAverageOfCube(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(find_Average_Of_Cube(5), 225.0/5, places=6)

    def test_edge_case_n_equals_zero(self):
        self.assertEqual(find_Average_Of_Cube(0), 0)

    def test_edge_case_n_equals_one(self):
        self.assertEqual(find_Average_Of_Cube(1), 1)

    def test_invalid_input_negative_number(self):
        with self.assertRaises(Exception):
            find_Average_Of_Cube(-5)

    def test_invalid_input_non_integer(self):
        with self.assertRaises(Exception):
            find_Average_Of_Cube(5.5)
