import unittest
from mbpp_279_code import is_num_decagonal

class TestIsNumDecagonal(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(is_num_decagonal(1), 1)
        self.assertEqual(is_num_decagonal(2), 10)
        self.assertEqual(is_num_decagonal(3), 27)

    def test_boundary_conditions(self):
        self.assertEqual(is_num_decagonal(0), 0)
        self.assertEqual(is_num_decagonal(100), 40000)

    def test_edge_cases(self):
        self.assertEqual(is_num_decagonal(-1), -3)
        self.assertEqual(is_num_decagonal(-100), -40000)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            is_num_decagonal('a')
        with self.assertRaises(TypeError):
            is_num_decagonal(None)
        with self.assertRaises(TypeError):
            is_num_decagonal([1, 2, 3])
