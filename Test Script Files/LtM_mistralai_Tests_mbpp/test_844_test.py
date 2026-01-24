import unittest
from mbpp_844_code import get_Number

class TestGetNumber(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(get_Number(3, 1), 1)
        self.assertEqual(get_Number(3, 2), 2)
        self.assertEqual(get_Number(3, 3), 3)

    def test_edge_and_boundary(self):
        self.assertEqual(get_Number(0, 1), 0)
        self.assertEqual(get_Number(1, 1), 1)
        self.assertEqual(get_Number(2, 1), 1)
        self.assertEqual(get_Number(2, 2), 2)
        self.assertEqual(get_Number(3, 4), 3)

    def test_complex_input(self):
        self.assertEqual(get_Number(4, 1), 1)
        self.assertEqual(get_Number(4, 2), 2)
        self.assertEqual(get_Number(4, 3), 3)
        self.assertEqual(get_Number(4, 4), 0)
