import unittest
from mbpp_279_code import is_num_decagonal

class TestIsNumDecagonal(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(is_num_decagonal(1), 0)
        self.assertEqual(is_num_decagonal(2), 12)
        self.assertEqual(is_num_decagonal(3), 36)

    def test_edge_cases(self):
        self.assertEqual(is_num_decagonal(0), 0)
        self.assertEqual(is_num_decagonal(10), 400)

    def test_boundary_conditions(self):
        self.assertEqual(is_num_decagonal(100), 40000)
        self.assertEqual(is_num_decagonal(1000), 4000000)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            is_num_decagonal('a')
        with self.assertRaises(TypeError):
            is_num_decagonal(None)
