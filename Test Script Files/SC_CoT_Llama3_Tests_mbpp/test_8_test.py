import unittest
from mbpp_8_code import square_nums

class TestSquareNums(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(square_nums([1, 2, 3, 4, 5]), [1, 4, 9, 16, 25])

    def test_edge_case_empty_list(self):
        self.assertEqual(square_nums([]), [])

    def test_edge_case_single_element(self):
        self.assertEqual(square_nums([10]), [100])

    def test_edge_case_negative_numbers(self):
        self.assertEqual(square_nums([-1, -2, -3]), [1, 4, 9])

    def test_edge_case_zero(self):
        self.assertEqual(square_nums([0, 0, 0]), [0, 0, 0])

    def test_edge_case_non_numeric_input(self):
        with self.assertRaises(TypeError):
            square_nums(['a', 'b', 'c'])

    def test_edge_case_mixed_input(self):
        with self.assertRaises(TypeError):
            square_nums([1, 2, 'a', 4])
