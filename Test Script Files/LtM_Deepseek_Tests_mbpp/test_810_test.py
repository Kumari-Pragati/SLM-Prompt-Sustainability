import unittest
from mbpp_810_code import count_variable

class TestCountVariable(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(count_variable(1, 2, 3, 4), ['p', 'q', 'r', 's'])

    def test_edge_conditions(self):
        self.assertEqual(count_variable(0, 0, 0, 0), ['p', 'q', 'r', 's'])
        self.assertEqual(count_variable(1, 2, 3, 4), ['p', 'q', 'r', 's'])
        self.assertEqual(count_variable(-1, -2, -3, -4), ['p', 'q', 'r', 's'])

    def test_boundary_conditions(self):
        self.assertEqual(count_variable(1000, 2000, 3000, 4000), ['p', 'q', 'r', 's'])
        self.assertEqual(count_variable(-1000, -2000, -3000, -4000), ['p', 'q', 'r', 's'])

    def test_complex_cases(self):
        self.assertEqual(count_variable(10, 20, 30, 40), ['p', 'q', 'r', 's'])
        self.assertEqual(count_variable(-10, -20, -30, -40), ['p', 'q', 'r', 's'])
