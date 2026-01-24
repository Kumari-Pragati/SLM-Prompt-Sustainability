import unittest
from mbpp_710_code import front_and_rear

class TestFrontAndRear(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(front_and_rear((1, 2, 3, 4, 5)), ((1, 5)))

    def test_single_element(self):
        self.assertEqual(front_and_rear((1,)), ((1, 1)))

    def test_empty_tuple(self):
        self.assertEqual(front_and_rear(()), ((), ()))

    def test_large_tuple(self):
        test_tup = tuple(range(1, 1001))
        self.assertEqual(front_and_rear(test_tup), ((1, 1000)))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            front_and_rear(123)
