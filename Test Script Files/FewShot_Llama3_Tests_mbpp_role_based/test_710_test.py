import unittest
from mbpp_710_code import front_and_rear

class TestFrontAndRear(unittest.TestCase):
    def test_typical_use_case(self):
        test_tup = (1, 2, 3, 4, 5)
        self.assertEqual(front_and_rear(test_tup), (1, 5))

    def test_empty_tuple(self):
        test_tup = ()
        self.assertEqual(front_and_rear(test_tup), ())

    def test_single_element_tuple(self):
        test_tup = (1,)
        self.assertEqual(front_and_rear(test_tup), (1,))

    def test_tuple_with_two_elements(self):
        test_tup = (1, 2)
        self.assertEqual(front_and_rear(test_tup), (1, 2))

    def test_tuple_with_three_elements(self):
        test_tup = (1, 2, 3)
        self.assertEqual(front_and_rear(test_tup), (1, 3))
