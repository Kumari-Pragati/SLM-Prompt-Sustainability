import unittest
from mbpp_710_code import front_and_rear

class TestFrontAndRear(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(front_and_rear((1, 2, 3, 4)), (1, 4))
        self.assertEqual(front_and_rear((5, 6, 7, 8, 9)), (5, 9))

    def test_edge_input(self):
        self.assertEqual(front_and_rear(()), ())
        self.assertEqual(front_and_rear((1,)), (1,))
        self.assertEqual(front_and_rear((1, 2)), (1, 2))
        self.assertEqual(front_and_rear((1, 2, 3)), (1, 3))

    def test_empty_list(self):
        self.assertEqual(front_and_rear([]), (None, None))

    def test_invalid_input(self):
        self.assertRaises(TypeError, front_and_rear, 123)
        self.assertRaises(TypeError, front_and_rear, {'a': 1, 'b': 2})
