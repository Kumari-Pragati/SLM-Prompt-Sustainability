import unittest
from mbpp_710_code import front_and_rear

class TestFrontAndRear(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(front_and_rear((1, 2, 3, 4, 5)), ((1, 5)))

    def test_single_element(self):
        self.assertEqual(front_and_rear((1,)), ((1, 1)))

    def test_empty_tuple(self):
        self.assertEqual(front_and_rear(()), ((), ()))

    def test_negative_numbers(self):
        self.assertEqual(front_and_rear((-1, -2, -3, -4, -5)), ((-1, -5)))

    def test_zero(self):
        self.assertEqual(front_and_rear((0, 1, 2, 3, 4, 5)), ((0, 5)))

    def test_large_numbers(self):
        self.assertEqual(front_and_rear((1000, 2000, 3000, 4000, 5000)), ((1000, 5000)))

    def test_non_integer_elements(self):
        self.assertEqual(front_and_rear((1.1, 2.2, 3.3, 4.4, 5.5)), ((1.1, 5.5)))

    def test_string_elements(self):
        self.assertEqual(front_and_rear(('a', 'b', 'c', 'd', 'e')), (('a', 'e')))

    def test_mixed_types(self):
        with self.assertRaises(TypeError):
            front_and_rear((1, 'a', 2.0))
