import unittest
from mbpp_844_code import get_Number

class TestGetNumber(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(get_Number(5, 1), 1)
        self.assertEqual(get_Number(5, 2), 2)
        self.assertEqual(get_Number(5, 3), 3)
        self.assertEqual(get_Number(5, 4), 4)
        self.assertEqual(get_Number(5, 5), 5)

    def test_edge_cases(self):
        self.assertEqual(get_Number(5, 6), 2)
        self.assertEqual(get_Number(5, 5), 5)
        self.assertEqual(get_Number(5, 0), None)

    def test_boundary_cases(self):
        self.assertEqual(get_Number(10, 1), 1)
        self.assertEqual(get_Number(10, 2), 2)
        self.assertEqual(get_Number(10, 3), 3)
        self.assertEqual(get_Number(10, 4), 4)
        self.assertEqual(get_Number(10, 5), 5)
        self.assertEqual(get_Number(10, 6), 6)
        self.assertEqual(get_Number(10, 7), 8)
        self.assertEqual(get_Number(10, 8), 10)
        self.assertEqual(get_Number(10, 9), 8)
        self.assertEqual(get_Number(10, 10), 10)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            get_Number("five", 1)
        with self.assertRaises(TypeError):
            get_Number(5, "one")
