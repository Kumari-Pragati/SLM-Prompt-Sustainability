import unittest
from mbpp_710_code import front_and_rear

class TestFrontAndRear(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(front_and_rear((1, 2, 3, 4, 5)), (1, 5))

    def test_empty_input(self):
        with self.assertRaises(IndexError):
            front_and_rear(())

    def test_single_element_input(self):
        self.assertEqual(front_and_rear((1,)), (1, 1))

    def test_tuple_with_duplicates(self):
        self.assertEqual(front_and_rear((1, 2, 2, 3, 1)), (1, 1))

    def test_negative_numbers(self):
        self.assertEqual(front_and_rear((-1, -2, -3, -4, -5)), (-1, -5))

    def test_mixed_type_input(self):
        with self.assertRaises(TypeError):
            front_and_rear((1, 'a', 3, 4, 5))
