import unittest
from103_code import eulerian_num

class TestEulerianNum(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(eulerian_num(0, 0), 1)
        self.assertEqual(eulerian_num(0, 1), 0)

    def test_negative(self):
        self.assertEqual(eulerian_num(-1, 0), 0)
        self.assertEqual(eulerian_num(0, -1), 0)

    def test_invalid_input(self):
        self.assertRaises(ValueError, eulerian_num, -1, 2)
        self.assertRaises(ValueError, eulerian_num, 1, -2)

    def test_small_values(self):
        self.assertEqual(eulerian_num(1, 0), 1)
        self.assertEqual(eulerian_num(1, 1), 1)
        self.assertEqual(eulerian_num(2, 1), 3)
        self.assertEqual(eulerian_num(2, 2), 2)

    def test_large_values(self):
        self.assertEqual(eulerian_num(10, 5), 147)
        self.assertEqual(eulerian_num(10, 10), 45)
