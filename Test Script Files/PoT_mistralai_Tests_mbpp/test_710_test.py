import unittest
from mbpp_710_code import front_and_rear

class TestFrontAndRear(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(front_and_rear((1, 2, 3, 4)), (1, 4))

    def test_edge_case_empty_list(self):
        self.assertEqual(front_and_rear([]), (None, None))

    def test_edge_case_single_element(self):
        self.assertEqual(front_and_rear([1]), (1, 1))

    def test_corner_case_negative_numbers(self):
        self.assertEqual(front_and_rear((-1, -2, -3, -4)), (-1, -4))
