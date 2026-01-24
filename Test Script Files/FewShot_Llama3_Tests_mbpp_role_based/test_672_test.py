import unittest
from mbpp_672_code import max_of_three

class TestMaxOfThree(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(max_of_three(1, 2, 3), 3)

    def test_edge_case_equal_numbers(self):
        self.assertEqual(max_of_three(1, 1, 1), 1)

    def test_edge_case_negative_numbers(self):
        self.assertEqual(max_of_three(-1, -2, -3), -1)

    def test_edge_case_zero(self):
        self.assertEqual(max_of_three(0, 0, 0), 0)

    def test_edge_case_mixed_signs(self):
        self.assertEqual(max_of_three(-1, 0, 1), 1)

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            max_of_three('a', 'b', 'c')
