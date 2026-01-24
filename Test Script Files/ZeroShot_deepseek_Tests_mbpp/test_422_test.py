import unittest
from mbpp_422_code import find_Average_Of_Cube

class TestFindAverageOfCube(unittest.TestCase):

    def test_find_Average_Of_Cube(self):
        self.assertAlmostEqual(find_Average_Of_Cube(1), 1.0, places=6)
        self.assertAlmostEqual(find_Average_Of_Cube(2), 4.5, places=6)
        self.assertAlmostEqual(find_Average_Of_Cube(3), 9.6, places=6)
        self.assertAlmostEqual(find_Average_Of_Cube(4), 16.0, places=6)
        self.assertAlmostEqual(find_Average_Of_Cube(5), 24.0, places=6)
