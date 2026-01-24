import unittest
from mbpp_710_code import front_and_rear

class TestFrontAndRear(unittest.TestCase):

    def test_typical(self):
        self.assertEqual(front_and_rear((1, 2, 3)), (1, 3))

    def test_empty(self):
        self.assertRaises(IndexError, front_and_rear, ())

    def test_single_element(self):
        self.assertEqual(front_and_rear((1,)), (1, 1))

    def test_multiple_elements(self):
        self.assertEqual(front_and_rear((1, 2, 3, 4, 5)), (1, 5))

    def test_negative_numbers(self):
        self.assertEqual(front_and_rear((-1, 2, -3)), (-1, -3))

    def test_mixed_types(self):
        self.assertEqual(front_and_rear((1, 'a', 3.0)), (1, 3.0))
