import unittest
from mbpp_797_code import sum_in_Range

class TestSumInRange(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(sum_in_Range(1, 10), 25)

    def test_boundary_conditions(self):
        self.assertEqual(sum_in_Range(1, 1), 1)
        self.assertEqual(sum_in_Range(1, 2), 4)

    def test_edge_conditions(self):
        self.assertEqual(sum_in_Range(1, 0), 0)
        self.assertEqual(sum_in_Range(1, -1), 0)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            sum_in_Range('1', 10)
        with self.assertRaises(TypeError):
            sum_in_Range(1, '10')
        with self.assertRaises(TypeError):
            sum_in_Range('1', '10')
