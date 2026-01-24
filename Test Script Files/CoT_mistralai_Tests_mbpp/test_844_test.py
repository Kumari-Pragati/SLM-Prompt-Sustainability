import unittest
from mbpp_844_code import get_Number

class TestGetNumber(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(get_Number(5, 3), 3)
        self.assertEqual(get_Number(10, 6), 8)
        self.assertEqual(get_Number(15, 13), 13)

    def test_edge_input(self):
        self.assertEqual(get_Number(0, 1), 0)
        self.assertEqual(get_Number(1, 1), 1)
        self.assertEqual(get_Number(2, 2), 2)
        self.assertEqual(get_Number(3, 3), 3)
        self.assertEqual(get_Number(4, 4), 4)

    def test_boundary_input(self):
        self.assertEqual(get_Number(1, 0), 0)
        self.assertEqual(get_Number(1, 5), 1)
        self.assertEqual(get_Number(2, 2), 2)
        self.assertEqual(get_Number(2, 3), 2)
        self.assertEqual(get_Number(3, 3), 3)
        self.assertEqual(get_Number(3, 4), 0)

    def test_invalid_input_k(self):
        self.assertRaises(IndexError, get_Number, 5, 6)
        self.assertRaises(IndexError, get_Number, 0, 1)
        self.assertRaises(IndexError, get_Number, 1, 0)
        self.assertRaises(IndexError, get_Number, -1, 1)
        self.assertRaises(IndexError, get_Number, 1, -1)

    def test_invalid_input_n(self):
        self.assertRaises(ValueError, get_Number, -1, 1)
        self.assertRaises(ValueError, get_Number, 0, 1)
