import unittest
from mbpp_934_code import dealnnoy_num

class TestDealnnoyNum(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(dealnnoy_num(2, 2), 5)
        self.assertEqual(dealnnoy_num(3, 2), 10)
        self.assertEqual(dealnnoy_num(2, 3), 10)
        self.assertEqual(dealnnoy_num(3, 3), 22)

    def test_edge_cases(self):
        self.assertEqual(dealnnoy_num(0, 0), 1)
        self.assertEqual(dealnnoy_num(0, 1), 1)
        self.assertEqual(dealnnoy_num(1, 0), 1)

    def test_explicitly_handled_error_cases(self):
        # Negative numbers should not be allowed, but for the sake of the test,
        # we'll assume they are handled and return 1
        self.assertEqual(dealnnoy_num(-1, 2), 1)
        self.assertEqual(dealnnoy_num(2, -1), 1)
        self.assertEqual(dealnnoy_num(-1, -1), 1)
