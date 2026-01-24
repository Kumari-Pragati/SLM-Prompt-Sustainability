import unittest
from mbpp_8_code import square_nums

class TestSquareNums(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(square_nums([1, 2, 3]), [1, 4, 9])

    def test_edge_condition(self):
        self.assertEqual(square_nums([0]), [0])

    def test_boundary_condition(self):
        self.assertEqual(square_nums([-1, 1]), [1, 1])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            square_nums("1, 2, 3")
