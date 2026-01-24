import unittest
from mbpp_641_code import is_nonagonal

class TestIsNonagonal(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(is_nonagonal(1), 1)
        self.assertEqual(is_nonagonal(2), 3)
        self.assertEqual(is_nonagonal(3), 6)
        self.assertEqual(is_nonagonal(4), 10)
        self.assertEqual(is_nonagonal(5), 15)

    def test_edge_and_boundary_cases(self):
        self.assertEqual(is_nonagonal(0), None)
        self.assertEqual(is_nonagonal(-1), None)
        self.assertEqual(is_nonagonal(6), 28)
        self.assertEqual(is_nonagonal(7), 36)

    def test_invalid_or_exceptional_inputs(self):
        with self.assertRaises(TypeError):
            is_nonagonal('a')
