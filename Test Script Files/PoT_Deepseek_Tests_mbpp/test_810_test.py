import unittest
from mbpp_810_code import count_variable

class TestCountVariable(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_variable(1, 2, 3, 4), [1, 2, 3, 4])

    def test_edge_case_with_zero(self):
        self.assertEqual(count_variable(0, 0, 0, 0), [0, 0, 0, 0])

    def test_boundary_case_with_max_int(self):
        self.assertEqual(count_variable(2**31-1, 2**31-1, 2**31-1, 2**31-1), 
                         [2**31-1, 2**31-1, 2**31-1, 2**31-1])

    def test_corner_case_with_negative_numbers(self):
        self.assertEqual(count_variable(-1, -2, -3, -4), [-1, -2, -3, -4])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            count_variable(1, 'two', 3, None)
