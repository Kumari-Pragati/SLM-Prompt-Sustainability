import unittest
from mbpp_422_code import find_Average_Of_Cube

class TestFindAverageOfCube(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_Average_Of_Cube(5), 12.5)

    def test_edge_case(self):
        self.assertEqual(find_Average_Of_Cube(1), 1.0)
        self.assertEqual(find_Average_Of_Cube(2), 2.8333333333333335)

    def test_edge_case_zero(self):
        with self.assertRaises(ZeroDivisionError):
            find_Average_Of_Cube(0)

    def test_edge_case_negative(self):
        with self.assertRaises(ValueError):
            find_Average_Of_Cube(-1)

    def test_edge_case_large(self):
        self.assertEqual(find_Average_Of_Cube(1000), 249.9999999999999)
