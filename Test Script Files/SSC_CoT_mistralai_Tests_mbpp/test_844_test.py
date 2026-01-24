import unittest
from mbpp_844_code import get_Number

class TestGetNumber(unittest.TestCase):

    def test_normal_case(self):
        self.assertEqual(get_Number(5, 3), 3)
        self.assertEqual(get_Number(10, 6), 8)

    def test_edge_cases(self):
        self.assertEqual(get_Number(1, 1), 1)
        self.assertEqual(get_Number(2, 1), 1)
        self.assertEqual(get_Number(2, 2), 2)
        self.assertEqual(get_Number(4, 1), 1)
        self.assertEqual(get_Number(4, 4), 4)
        self.assertEqual(get_Number(4, 5), None)

    def test_boundary_cases(self):
        self.assertEqual(get_Number(0, 0), None)
        self.assertEqual(get_Number(1, 0), None)
        self.assertEqual(get_Number(1, 1), 1)
        self.assertEqual(get_Number(2, 2), 2)
        self.assertEqual(get_Number(3, 3), 3)
        self.assertEqual(get_Number(4, 4), 4)
        self.assertEqual(get_Number(5, 5), 5)
