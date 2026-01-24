import unittest
from mbpp_279_code import is_num_decagonal

class TestIsNumDecagonal(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(is_num_decagonal(1), 1)
        self.assertEqual(is_num_decagonal(2), 3)
        self.assertEqual(is_num_decagonal(3), 15)
        self.assertEqual(is_num_decagonal(4), 39)

    def test_edge_cases(self):
        self.assertEqual(is_num_decagonal(0), 0)
        self.assertEqual(is_num_decagonal(-1), None)
        self.assertEqual(is_num_decagonal(0.5), None)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            is_num_decagonal('a')
        with self.assertRaises(TypeError):
            is_num_decagonal(None)
