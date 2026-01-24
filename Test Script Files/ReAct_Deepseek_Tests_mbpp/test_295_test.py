import unittest
from mbpp_295_code import sum_div

class TestSumDiv(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(sum_div(6), 6)
        self.assertEqual(sum_div(28), 28)
        self.assertEqual(sum_div(12), 15)

    def test_edge_cases(self):
        self.assertEqual(sum_div(1), 1)
        self.assertEqual(sum_div(0), 0)
        self.assertEqual(sum_div(-10), 0)

    def test_explicitly_handled_error_cases(self):
        with self.assertRaises(TypeError):
            sum_div("10")
        with self.assertRaises(TypeError):
            sum_div(None)
