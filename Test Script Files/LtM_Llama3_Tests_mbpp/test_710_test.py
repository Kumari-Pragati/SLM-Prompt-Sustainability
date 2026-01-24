import unittest
from mbpp_710_code import front_and_rear

class TestFrontAndRear(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(front_and_rear((1, 2, 3)), (1, 3))

    def test_empty_input(self):
        with self.assertRaises(IndexError):
            front_and_rear(())

    def test_single_element_input(self):
        self.assertEqual(front_and_rear((1,)), (1, 1))

    def test_tuple_with_duplicates(self):
        self.assertEqual(front_and_rear((1, 2, 2, 3)), (1, 3))

    def test_tuple_with_negative_numbers(self):
        self.assertEqual(front_and_rear((-1, 2, -3)), (-1, -3))

    def test_tuple_with_mixed_types(self):
        self.assertEqual(front_and_rear((1, 'a', 3.0)), (1, 3.0))
