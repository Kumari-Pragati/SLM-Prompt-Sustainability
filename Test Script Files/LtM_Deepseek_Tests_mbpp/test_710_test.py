import unittest
from mbpp_710_code import front_and_rear

class TestFrontAndRear(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(front_and_rear((1, 2, 3)), ((1, 3),))

    def test_empty_input(self):
        self.assertEqual(front_and_rear(()), ((),))

    def test_single_element_input(self):
        self.assertEqual(front_and_rear((5,)), ((5,),))

    def test_large_input(self):
        large_tuple = tuple(range(1, 1001))
        self.assertEqual(front_and_rear(large_tuple), (large_tuple[0], large_tuple[-1]))

    def test_negative_numbers(self):
        self.assertEqual(front_and_rear((-1, -2, -3)), ((-1, -3),))

    def test_mixed_types(self):
        self.assertEqual(front_and_rear((1, 'two', 3.0)), ((1, 'two'),))
