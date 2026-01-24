import unittest
from mbpp_710_code import front_and_rear

class TestFrontAndRear(unittest.TestCase):
    def test_typical_input(self):
        test_tup = (1, 2, 3, 4, 5)
        result = front_and_rear(test_tup)
        self.assertEqual(result, (1, 5))

    def test_empty_input(self):
        test_tup = ()
        result = front_and_rear(test_tup)
        self.assertEqual(result, ())

    def test_single_element_input(self):
        test_tup = (1,)
        result = front_and_rear(test_tup)
        self.assertEqual(result, (1, 1))

    def test_negative_numbers_input(self):
        test_tup = (-1, 2, -3, 4, -5)
        result = front_and_rear(test_tup)
        self.assertEqual(result, (-1, -5))

    def test_non_integer_input(self):
        test_tup = ('a', 'b', 'c', 'd', 'e')
        with self.assertRaises(TypeError):
            front_and_rear(test_tup)

    def test_mixed_type_input(self):
        test_tup = (1, 'b', 3, 'd', 5)
        result = front_and_rear(test_tup)
        self.assertEqual(result, (1, 5))
