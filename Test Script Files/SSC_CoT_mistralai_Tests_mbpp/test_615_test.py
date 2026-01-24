import unittest
from mbpp_615_code import average_tuple

class TestAverageTuple(unittest.TestCase):

    def test_normal_input(self):
        self.assertListEqual(average_tuple([(1, 2, 3), (4, 5, 6), (7, 8, 9)]), [2.3333333333333337, 5.0, 6.333333333333333])

    def test_empty_input(self):
        self.assertListEqual(average_tuple([]), [])

    def test_single_input(self):
        self.assertListEqual(average_tuple([(1)]), [1.0])

    def test_single_element_input(self):
        self.assertListEqual(average_tuple([(1,)]), [1.0])

    def test_negative_numbers(self):
        self.assertListEqual(average_tuple([(-1, 2, -3), (4, -5, 6), (-7, 8, -9)]), [-0.3333333333333333, -1.0, -3.333333333333333])

    def test_zero_numbers(self):
        self.assertListEqual(average_tuple([(0, 2, 0), (0, 0, 0)]), [0.0, nan])
