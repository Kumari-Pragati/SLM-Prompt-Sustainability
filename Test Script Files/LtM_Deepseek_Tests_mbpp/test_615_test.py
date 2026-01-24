import unittest
from mbpp_615_code import average_tuple

class TestAverageTuple(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(average_tuple([(1, 2, 3), (4, 5, 6)]), [2.5, 3.5, 4.5])

    def test_empty_input(self):
        self.assertEqual(average_tuple([]), [])

    def test_single_tuple_input(self):
        self.assertEqual(average_tuple([(1, 2, 3)]), [1.0, 2.0, 3.0])

    def test_negative_numbers(self):
        self.assertEqual(average_tuple([(-1, -2, -3), (-4, -5, -6)]), [-2.5, -3.5, -4.5])

    def test_mixed_numbers(self):
        self.assertEqual(average_tuple([(1, 2, 3), (4, 5, 6), (-1, -2, -3)]), [1.0, 2.0, 1.0])

    def test_different_length_tuples(self):
        self.assertEqual(average_tuple([(1, 2), (3, 4, 5)]), [1.5, 3.5])
