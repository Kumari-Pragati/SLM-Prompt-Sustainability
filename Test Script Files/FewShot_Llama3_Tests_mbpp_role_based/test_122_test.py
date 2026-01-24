import unittest
from mbpp_122_code import smartNumber

class TestSmartNumber(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(smartNumber(1), 2)

    def test_edge_case_max(self):
        self.assertEqual(smartNumber(3000), 2999)

    def test_edge_case_min(self):
        self.assertEqual(smartNumber(1), 2)

    def test_invalid_input(self):
        with self.assertRaises(IndexError):
            smartNumber(3001)

    def test_edge_case_zero(self):
        with self.assertRaises(IndexError):
            smartNumber(0)

    def test_edge_case_negative(self):
        with self.assertRaises(IndexError):
            smartNumber(-1)
