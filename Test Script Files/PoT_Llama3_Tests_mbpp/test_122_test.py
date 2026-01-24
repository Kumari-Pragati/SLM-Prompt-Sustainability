import unittest
from mbpp_122_code import smartNumber

class TestSmartNumber(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(smartNumber(1), 2)

    def test_edge_case(self):
        self.assertEqual(smartNumber(3000), 2998)

    def test_edge_case2(self):
        self.assertEqual(smartNumber(1), 2)

    def test_edge_case3(self):
        self.assertEqual(smartNumber(3000), 2998)

    def test_edge_case4(self):
        self.assertEqual(smartNumber(0), None)

    def test_edge_case5(self):
        with self.assertRaises(IndexError):
            smartNumber(3001)

    def test_edge_case6(self):
        with self.assertRaises(IndexError):
            smartNumber(0)
