import unittest
from mbpp_710_code import front_and_rear

class TestFrontAndRear(unittest.TestCase):

    def test_front_and_rear(self):
        self.assertEqual(front_and_rear((1, 2, 3, 4, 5)), (1, 5))
        self.assertEqual(front_and_rear((-1, 2, 3, 4, 5)), (-1, 5))
        self.assertEqual(front_and_rear(('a', 'b', 'c', 'd', 'e')), ('a', 'e'))
        self.assertEqual(front_and_rear((1, 2, 3, 4, 5, 6)), (1, 6))
        self.assertEqual(front_and_rear((-1, -2, -3, -4, -5)), (-1, -5))

    def test_empty_input(self):
        with self.assertRaises(IndexError):
            front_and_rear(())

    def test_single_element_input(self):
        with self.assertRaises(IndexError):
            front_and_rear((1,))
