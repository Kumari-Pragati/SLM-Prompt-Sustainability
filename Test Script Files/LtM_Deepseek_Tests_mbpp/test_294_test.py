import unittest
from mbpp_294_code import max_val

class TestMaxVal(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(max_val([1, 2, 3, 4, 5]), 5)
        self.assertEqual(max_val([10, 20, 30, 40, 50]), 50)

    def test_edge_conditions(self):
        self.assertEqual(max_val([-1, -2, -3, -4, -5]), -1)
        self.assertEqual(max_val([0, -1, -2, -3, -4]), 0)
        self.assertEqual(max_val([1]), 1)
        self.assertIsNone(max_val([]))

    def test_complex_cases(self):
        self.assertEqual(max_val([1, 2, 3, 'a', 4, 5]), 5)
        self.assertEqual(max_val([1, 2, 3, None, 4, 5]), 5)
        self.assertEqual(max_val([1, 2, 3, [4, 5], 6]), 6)
        self.assertEqual(max_val([1, 2, 3, {'a': 4}, 5]), 5)
