import unittest
from mbpp_790_code import even_position

class TestEvenPosition(unittest.TestCase):

    def test_simple_valid_inputs(self):
        self.assertTrue(even_position([0, 1, 2, 3]))
        self.assertTrue(even_position([2, 3, 4, 5]))

    def test_edge_conditions(self):
        self.assertTrue(even_position([]))
        self.assertTrue(even_position([0]))
        self.assertTrue(even_position([2, 0]))

    def test_complex_cases(self):
        self.assertFalse(even_position([0, 1]))
        self.assertFalse(even_position([1, 2]))
        self.assertFalse(even_position([0, 2]))
        self.assertFalse(even_position([1, 3]))
