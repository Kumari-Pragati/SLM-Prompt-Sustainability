import unittest
from mbpp_710_code import front_and_rear

class TestFrontAndRear(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(front_and_rear((1, 2, 3, 4)), (1, 4))
        self.assertEqual(front_and_rear((5, 6, 7, 8)), (5, 8))

    def test_empty_input(self):
        self.assertEqual(front_and_rear(()), (None, None))

    def test_single_element_input(self):
        self.assertEqual(front_and_rear((1,)), (1, 1))

    def test_min_max_values(self):
        self.assertEqual(front_and_rear((-100, -99, -98, -97)), (-100, -97))
        self.assertEqual(front_and_rear((99, 100, 101, 102)), (99, 102))
