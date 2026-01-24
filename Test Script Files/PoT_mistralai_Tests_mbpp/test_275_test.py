import unittest
from mbpp_275_code import get_Position

class TestGetPosition(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(get_Position([1, 2, 3, 4], 4, 2), 3)
        self.assertEqual(get_Position([5, 10, 15, 20], 4, 5), 4)
        self.assertEqual(get_Position([-1, 0, 1, 2], 4, 1), 4)

    def test_edge_case_zero(self):
        self.assertEqual(get_Position([], 1, 1), 1)
        self.assertEqual(get_Position([0], 1, 1), 1)

    def test_edge_case_one(self):
        self.assertEqual(get_Position([1], 1, 1), 1)

    def test_edge_case_negative(self):
        self.assertEqual(get_Position([-1], 1, 1), None)

    def test_edge_case_negative_num_and_mod(self):
        self.assertEqual(get_Position([-1], -1, 1), None)
        self.assertEqual(get_Position([-1], 1, -1), None)

    def test_edge_case_zero_mod(self):
        self.assertEqual(get_Position([0], 1, 2), None)

    def test_corner_case_max_value(self):
        max_value = (1 << 31) - 1
        self.assertEqual(get_Position([max_value], 1, 2), None)
