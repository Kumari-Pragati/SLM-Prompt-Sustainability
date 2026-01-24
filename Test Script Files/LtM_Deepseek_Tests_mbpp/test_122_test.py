import unittest
from mbpp_122_code import smartNumber

class TestSmartNumber(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(smartNumber(1), 2)
        self.assertEqual(smartNumber(2), 3)
        self.assertEqual(smartNumber(3), 5)
        self.assertEqual(smartNumber(4), 7)
        self.assertEqual(smartNumber(5), 11)

    def test_edge_conditions(self):
        self.assertEqual(smartNumber(1), 2)
        self.assertEqual(smartNumber(2), 3)
        self.assertEqual(smartNumber(3), 5)
        self.assertEqual(smartNumber(4), 7)
        self.assertEqual(smartNumber(5), 11)

    def test_complex_cases(self):
        self.assertEqual(smartNumber(10), 29)
        self.assertEqual(smartNumber(20), 59)
        self.assertEqual(smartNumber(30), 101)
        self.assertEqual(smartNumber(40), 149)
        self.assertEqual(smartNumber(50), 199)
