import unittest
from mbpp_422_code import find_Average_Of_Cube

class TestFindAverageOfCube(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_Average_Of_Cube(5), 72.5)

    def test_edge_case(self):
        self.assertEqual(find_Average_Of_Cube(1), 1.0)
        self.assertEqual(find_Average_Of_Cube(2), 8.0)

    def test_edge_case2(self):
        self.assertEqual(find_Average_Of_Cube(0), 0.0)

    def test_edge_case3(self):
        self.assertEqual(find_Average_Of_Cube(3), 14.5)

    def test_edge_case4(self):
        self.assertEqual(find_Average_Of_Cube(4), 24.0)

    def test_edge_case5(self):
        self.assertEqual(find_Average_Of_Cube(100), 2500.0)

    def test_edge_case6(self):
        self.assertEqual(find_Average_Of_Cube(1000), 250000.0)

    def test_edge_case7(self):
        self.assertEqual(find_Average_Of_Cube(10000), 2500000.0)

    def test_edge_case8(self):
        self.assertEqual(find_Average_Of_Cube(100000), 25000000.0)
