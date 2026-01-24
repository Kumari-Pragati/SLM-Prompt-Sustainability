import unittest
from mbpp_655_code import fifth_Power_Sum

class TestFifthPowerSum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(fifth_Power_Sum(1), 1)
        self.assertEqual(fifth_Power_Sum(2), 2**5 + 1)
        self.assertEqual(fifth_Power_Sum(3), 3**5 + 2**5 + 1)
        self.assertEqual(fifth_Power_Sum(4), 4**5 + 3**5 + 2**5 + 1)

    def test_edge_cases(self):
        self.assertEqual(fifth_Power_Sum(0), 0)
        self.assertEqual(fifth_Power_Sum(1000), sum([i**5 for i in range(1, 1001)]) )
        self.assertEqual(fifth_Power_Sum(math.inf), math.inf)

    def test_negative_input(self):
        with self.assertRaises(ValueError):
            fifth_Power_Sum(-1)
