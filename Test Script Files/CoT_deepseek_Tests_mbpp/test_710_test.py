import unittest
from mbpp_710_code import front_and_rear

class TestFrontAndRear(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(front_and_rear((1, 2, 3, 4, 5)), ((1, 5)))

    def test_single_element(self):
        self.assertEqual(front_and_rear((1,)), ((1, 1)))

    def test_empty_tuple(self):
        self.assertEqual(front_and_rear(()), ((),))

    def test_large_tuple(self):
        test_tuple = tuple(range(1, 1001))
        self.assertEqual(front_and_rear(test_tuple), ((1, 1000)))

    def test_negative_numbers(self):
        self.assertEqual(front_and_rear((-1, -2, -3, -4, -5)), ((-1, -5)))

    def test_non_integer_elements(self):
        self.assertEqual(front_and_rear(('a', 'b', 'c', 'd', 'e')), (('a', 'e')))

    def test_non_tuple_input(self):
        with self.assertRaises(TypeError):
            front_and_rear("not a tuple")
