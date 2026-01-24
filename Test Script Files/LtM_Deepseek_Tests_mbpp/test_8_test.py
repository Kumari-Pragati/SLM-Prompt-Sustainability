import unittest
from mbpp_8_code import square_nums

class TestSquareNums(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(square_nums([1, 2, 3]), [1, 4, 9])
        self.assertEqual(square_nums([-1, 0, 1]), [1, 0, 1])

    def test_edge_conditions(self):
        self.assertEqual(square_nums([]), [])
        self.assertEqual(square_nums([0]), [0])

    def test_complex_cases(self):
        self.assertEqual(square_nums([-5, -3, -2]), [25, 9, 4])
        self.assertEqual(square_nums([10, 20, 30]), [100, 400, 900])
