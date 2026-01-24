import unittest
from mbpp_613_code import maximum_value

class TestMaximumValue(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(maximum_value([(1, [1, 2, 3])]), [(1, 3)])
        self.assertEqual(maximum_value([(2, [4, 5, 6])]), [(2, 6)])

    def test_edge_conditions(self):
        self.assertEqual(maximum_value([(1, [])]), [(1, None)])
        self.assertEqual(maximum_value([]), [])

    def test_complex_cases(self):
        self.assertEqual(maximum_value([(1, [1, 2, 3]), (2, [4, 5, 6])]), [(1, 3), (2, 6)])
        self.assertEqual(maximum_value([(1, [1, 2, 3]), (2, [])]), [(1, 3), (2, None)])
