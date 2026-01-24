import unittest
from mbpp_810_code import count_variable

class TestCountVariable(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(count_variable(2, 3, 4, 5), ['p', 'p', 'q', 'q', 'r', 'r', 's', 's'])

    def test_edge_case(self):
        self.assertEqual(count_variable(0, 0, 0, 0), [])

    def test_boundary_case(self):
        self.assertEqual(count_variable(1, 1, 1, 1), ['p', 'q', 'r', 's'])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            count_variable('a', 'b', 'c', 'd')
