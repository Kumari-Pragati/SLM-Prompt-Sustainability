import unittest
from mbpp_844_code import get_Number

class TestGetNumber(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(get_Number(5, 3), 3)
        self.assertEqual(get_Number(6, 4), 4)
        self.assertEqual(get_Number(7, 2), 1)
        self.assertEqual(get_Number(7, 7), 7)

    def test_edge_case(self):
        self.assertEqual(get_Number(0, 1), 0)
        self.assertEqual(get_Number(1, 1), 1)
        self.assertEqual(get_Number(2, 2), 2)
        self.assertEqual(get_Number(3, 3), 3)

    def test_boundary_case(self):
        self.assertEqual(get_Number(4, 1), 1)
        self.assertEqual(get_Number(4, 4), 4)
        self.assertEqual(get_Number(5, 5), 5)
        self.assertEqual(get_Number(6, 6), 6)
