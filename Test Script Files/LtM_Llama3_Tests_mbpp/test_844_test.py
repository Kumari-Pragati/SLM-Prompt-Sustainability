import unittest
from mbpp_844_code import get_Number

class TestGetNumber(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(get_Number(5, 1), 1)
        self.assertEqual(get_Number(5, 2), 2)
        self.assertEqual(get_Number(5, 3), 3)
        self.assertEqual(get_Number(5, 4), 4)
        self.assertEqual(get_Number(5, 5), 5)

    def test_edge(self):
        self.assertEqual(get_Number(5, 0), None)
        self.assertEqual(get_Number(5, 6), None)
        self.assertEqual(get_Number(1, 1), 1)
        self.assertEqual(get_Number(2, 1), 1)

    def test_complex(self):
        self.assertEqual(get_Number(10, 5), 5)
        self.assertEqual(get_Number(10, 10), 10)
        self.assertEqual(get_Number(10, 3), 3)
