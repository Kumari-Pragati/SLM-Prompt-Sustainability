import unittest
from mbpp_615_code import average_tuple

class TestAverageTuple(unittest.TestCase):

    def test_average_tuple_empty_list(self):
        self.assertListEqual(average_tuple([]), [])

    def test_average_tuple_single_list(self):
        self.assertListEqual(average_tuple([[1]]), [1.0])

    def test_average_tuple_multiple_lists(self):
        self.assertListEqual(average_tuple([[1, 2], [3, 4], [5, 6]]), [2.0, 4.0, 5.0])

    def test_average_tuple_mixed_types(self):
        self.assertRaises(TypeError, average_tuple, [[1, 2], [3, 'x'], [5, 6]])

    def test_average_tuple_negative_numbers(self):
        self.assertListEqual(average_tuple([[-1, -2], [3, -4], [-5, 6]]), [-1.0, -2.0, 0.5])

    def test_average_tuple_zero_length_sublists(self):
        self.assertListEqual(average_tuple([[0], [1, 2], [3, 4, 0]]), [0.0, 1.5, 3.0])
