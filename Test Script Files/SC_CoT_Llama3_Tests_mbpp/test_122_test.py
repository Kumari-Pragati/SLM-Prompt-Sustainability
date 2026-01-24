import unittest
from mbpp_122_code import smartNumber

class TestSmartNumber(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(smartNumber(1), 2)
        self.assertEqual(smartNumber(2), 3)
        self.assertEqual(smartNumber(3), 5)
        self.assertEqual(smartNumber(4), 7)
        self.assertEqual(smartNumber(5), 11)

    def test_edge_cases(self):
        self.assertRaises(IndexError, smartNumber, 0)
        self.assertRaises(IndexError, smartNumber, 3010)
        self.assertEqual(smartNumber(1), 2)
        self.assertEqual(smartNumber(2), 3)
        self.assertEqual(smartNumber(3), 5)
        self.assertEqual(smartNumber(4), 7)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            smartNumber('a')
        with self.assertRaises(TypeError):
            smartNumber(None)

    def test_corner_cases(self):
        self.assertEqual(smartNumber(10), 17)
        self.assertEqual(smartNumber(20), 29)
        self.assertEqual(smartNumber(30), 41)
