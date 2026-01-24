import unittest
from mbpp_122_code import smartNumber

class TestSmartNumber(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(smartNumber(1), 2)
        self.assertEqual(smartNumber(2), 3)
        self.assertEqual(smartNumber(3), 5)

    def test_edge_case(self):
        self.assertEqual(smartNumber(3000), 2999)

    def test_out_of_range(self):
        with self.assertRaises(IndexError):
            smartNumber(3001)

    def test_zero_input(self):
        with self.assertRaises(IndexError):
            smartNumber(0)

    def test_negative_input(self):
        with self.assertRaises(IndexError):
            smartNumber(-1)
