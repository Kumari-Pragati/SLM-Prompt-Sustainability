import unittest
from mbpp_615_code import average_tuple

class TestAverageTuple(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual(average_tuple([]), [])

    def test_single_element_list(self):
        self.assertAlmostEqual(average_tuple([(1,)]), [1.0])

    def test_single_value_list(self):
        self.assertAlmostEqual(average_tuple([[1], [2], [3]]), [1.0, 2.0, 3.0])

    def test_mixed_length_lists(self):
        self.assertListEqual(average_tuple([[1, 2], [3], [4, 5, 6]]), [2.0, 3.0, 4.5])

    def test_negative_numbers(self):
        self.assertAlmostEqual(average_tuple([[-1, 2], [3, -4], [5, -6]]), [0.0, 1.5, 0.5])

    def test_zero_numbers(self):
        self.assertListEqual(average_tuple([[0, 0], [0], [0, 0]]), [0.0, 0.0, 0.0])

    def test_large_numbers(self):
        self.assertAlmostEqual(average_tuple([[1e9, 2e9], [3e9, 4e9], [5e9, 6e9]]), [3.0e9, 4.0e9])
