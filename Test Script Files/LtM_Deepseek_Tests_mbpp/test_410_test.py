import unittest
from mbpp_410_code import min_val

class TestMinVal(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(min_val([1, 2, 3, 4, 5]), 1)
        self.assertEqual(min_val([10, 20, 30, 40, 50]), 10)

    def test_edge_conditions(self):
        self.assertEqual(min_val([1]), 1)
        self.assertIsNone(min_val([]))
        self.assertIsNone(min_val(['a', 'b', 'c']))
        self.assertIsNone(min_val([1, 'a', 'b', 'c']))

    def test_complex_cases(self):
        self.assertEqual(min_val([10, 20, 'a', 'b', 'c', 5]), 5)
        self.assertEqual(min_val([10, 20, None, 'b', 'c', 5]), 5)
        self.assertIsNone(min_val([None, 'a', 'b', 'c']))
