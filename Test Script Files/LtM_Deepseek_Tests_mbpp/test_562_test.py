import unittest
from mbpp_562_code import Find_Max_Length

class TestFindMaxLength(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(Find_Max_Length(['abc', 'def']), 3)
        self.assertEqual(Find_Max_Length(['123', '456789']), 7)

    def test_edge_conditions(self):
        self.assertEqual(Find_Max_Length([]), 0)
        self.assertEqual(Find_Max_Length(['']), 0)
        self.assertEqual(Find_Max_Length(['a']), 1)

    def test_complex_cases(self):
        self.assertEqual(Find_Max_Length(['abc', 'defg', 'hijk']), 4)
        self.assertEqual(Find_Max_Length(['1234567890', '12345678901234567890']), 20)
