import unittest
from mbpp_122_code import smartNumber

class TestSmartNumber(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(smartNumber(1), 2)
        self.assertEqual(smartNumber(2), 3)
        self.assertEqual(smartNumber(3), 5)
        self.assertEqual(smartNumber(4), 7)
        self.assertEqual(smartNumber(5), 11)
        self.assertEqual(smartNumber(6), 13)
        self.assertEqual(smartNumber(7), 17)
        self.assertEqual(smartNumber(8), 19)
        self.assertEqual(smartNumber(9), 23)
        self.assertEqual(smartNumber(10), 29)

    def test_edge(self):
        self.assertEqual(smartNumber(0), None)
        self.assertEqual(smartNumber(1), 2)
        self.assertEqual(smartNumber(3000), 2999)

    def test_invalid(self):
        with self.assertRaises(IndexError):
            smartNumber(-1)
        with self.assertRaises(IndexError):
            smartNumber(3001)
