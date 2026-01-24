import unittest
from mbpp_844_code import get_Number

class TestGetNumber(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(get_Number(5, 1), 1)
        self.assertEqual(get_Number(5, 2), 2)
        self.assertEqual(get_Number(5, 3), 4)
        self.assertEqual(get_Number(5, 4), 6)
        self.assertEqual(get_Number(5, 5), 8)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(get_Number(1, 1), 1)
        self.assertEqual(get_Number(2, 1), 1)
        self.assertEqual(get_Number(2, 2), 2)
        self.assertEqual(get_Number(3, 1), 1)
        self.assertEqual(get_Number(3, 2), 2)
        self.assertEqual(get_Number(3, 3), 4)

    def test_corner_cases(self):
        self.assertEqual(get_Number(10, 1), 1)
        self.assertEqual(get_Number(10, 10), 20)
        self.assertEqual(get_Number(10, 5), 10)
        self.assertEqual(get_Number(10, 6), 12)
        self.assertEqual(get_Number(10, 11), 22)
