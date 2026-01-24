import unittest
from mbpp_95_code import Find_Min_Length

class TestFindMinLength(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(Find_Min_Length(['abc', 'def', 'ghi']), 3)
        self.assertEqual(Find_Min_Length(['123', '456', '789']), 1)

    def test_edge_conditions(self):
        self.assertEqual(Find_Min_Length(['']), 0)
        self.assertEqual(Find_Min_Length(['a']), 1)
        self.assertEqual(Find_Min_Length(['abc', '']), 3)
        self.assertEqual(Find_Min_Length(['abc', 'def', 'ghi', '']), 0)

    def test_complex_cases(self):
        self.assertEqual(Find_Min_Length(['abc', 'defgh', 'ijklm']), 2)
        self.assertEqual(Find_Min_Length(['123456', '789101112', '1314151617181920']), 1)
