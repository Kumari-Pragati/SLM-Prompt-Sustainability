import unittest
from mbpp_125_code import find_length

class TestFindLength(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(find_length('10101', 5), 3)
        self.assertEqual(find_length('01010', 5), 2)
        self.assertEqual(find_length('11111', 5), 4)
        self.assertEqual(find_length('00000', 5), 0)

    def test_edge_case(self):
        self.assertEqual(find_length('1', 1), 0)
        self.assertEqual(find_length('0', 1), 0)
        self.assertEqual(find_length('10', 2), 1)
        self.assertEqual(find_length('01', 2), 1)
        self.assertEqual(find_length('11', 2), 1)
        self.assertEqual(find_length('00', 2), 0)

    def test_boundary_case(self):
        self.assertEqual(find_length('10101', 1), 0)
        self.assertEqual(find_length('01010', 1), 0)
        self.assertEqual(find_length('11111', 1), 0)
        self.assertEqual(find_length('00000', 1), 0)
        self.assertEqual(find_length('1', 0), 0)
        self.assertEqual(find_length('0', 0), 0)
