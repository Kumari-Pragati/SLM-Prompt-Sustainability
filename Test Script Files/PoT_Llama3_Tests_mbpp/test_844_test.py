import unittest
from mbpp_844_code import get_Number

class TestGetNumber(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(get_Number(5, 1), 1)
        self.assertEqual(get_Number(5, 2), 2)
        self.assertEqual(get_Number(5, 3), 4)
        self.assertEqual(get_Number(5, 4), 3)
        self.assertEqual(get_Number(5, 5), 5)

    def test_edge_case(self):
        self.assertEqual(get_Number(1, 1), 1)
        self.assertEqual(get_Number(2, 1), 1)
        self.assertEqual(get_Number(2, 2), 2)
        self.assertEqual(get_Number(3, 1), 1)
        self.assertEqual(get_Number(3, 2), 2)
        self.assertEqual(get_Number(3, 3), 3)

    def test_boundary_case(self):
        self.assertEqual(get_Number(4, 1), 1)
        self.assertEqual(get_Number(4, 2), 2)
        self.assertEqual(get_Number(4, 3), 3)
        self.assertEqual(get_Number(4, 4), 4)

    def test_invalid_input(self):
        with self.assertRaises(IndexError):
            get_Number(5, 6)
