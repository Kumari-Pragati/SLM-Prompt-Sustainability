import unittest
from mbpp_615_code import average_tuple

class TestAverageTuple(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(average_tuple([[1, 2, 3], [4, 5, 6]]), [2.5, 5.5])

    def test_empty_input(self):
        with self.assertRaises(ZeroDivisionError):
            average_tuple([])

    def test_single_input(self):
        self.assertEqual(average_tuple([[1, 2, 3]]), [2.0])

    def test_zero_sum(self):
        self.assertEqual(average_tuple([[0, 0, 0], [0, 0, 0]]), [0.0])

    def test_negative_numbers(self):
        self.assertEqual(average_tuple([[-1, -2, -3], [4, 5, 6]]), [1.0, 5.5])

    def test_non_integer_numbers(self):
        self.assertEqual(average_tuple([[1.5, 2.5, 3.5], [4.5, 5.5, 6.5]]), [2.5, 5.5])
