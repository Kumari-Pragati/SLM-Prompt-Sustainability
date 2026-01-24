import unittest
from mbpp_294_code import max_val

class TestMaxVal(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(max_val([1, 2, 3, 4, 5]), 5)

    def test_edge_condition(self):
        self.assertEqual(max_val([-1, -2, -3, -4, -5]), -1)

    def test_boundary_condition(self):
        self.assertEqual(max_val([0]), 0)

    def test_mixed_types(self):
        self.assertEqual(max_val([1, 2, '3', 4.0, 5]), 5)

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            max_val([])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            max_val('1,2,3,4,5')
