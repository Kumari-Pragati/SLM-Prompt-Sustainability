import unittest
from mbpp_253_code import count_integer

class TestCountInteger(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(count_integer([1, 2, 3]), 3)
        self.assertEqual(count_integer([10, 20, 30]), 3)
        self.assertEqual(count_integer([-1, -2, -3]), 3)

    def test_edge_conditions(self):
        self.assertEqual(count_integer([]), 0)
        self.assertEqual(count_integer([1]), 1)
        self.assertEqual(count_integer([1, 2, 'a', 'b', 3]), 3)
        self.assertEqual(count_integer([1, 2, None, 3]), 2)

    def test_complex_cases(self):
        self.assertEqual(count_integer([1, 2, None, 'a', 'b', 3]), 3)
        self.assertEqual(count_integer([1, 2, 'a', 'b', None, 3]), 2)
        self.assertEqual(count_integer([None, None, None]), 0)
        self.assertEqual(count_integer(['a', 'b', 'c']), 0)
