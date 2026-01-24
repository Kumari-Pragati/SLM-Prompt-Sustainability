import unittest
from mbpp_341_code import set_to_tuple

class TestSetToTuple(unittest.TestCase):

    def test_set_to_tuple(self):
        self.assertEqual(set_to_tuple({1, 2, 3}), (1, 2, 3))
        self.assertEqual(set_to_tuple({3, 2, 1}), (1, 2, 3))
        self.assertEqual(set_to_tuple({1, 2, 2, 3}), (1, 2, 3))
        self.assertEqual(set_to_tuple({1, 1, 1, 2, 2, 3}), (1, 2, 3))
        self.assertEqual(set_to_tuple({}), ())
        self.assertEqual(set_to_tuple({1}), (1,))
        self.assertEqual(set_to_tuple({1, 2}), (1, 2))
        self.assertEqual(set_to_tuple({1, 2, 3, 4}), (1, 2, 3, 4))
        self.assertEqual(set_to_tuple({1, 2, 3, 4, 5}), (1, 2, 3, 4, 5))
        self.assertEqual(set_to_tuple({1, 2, 3, 4, 5, 6}), (1, 2, 3, 4, 5, 6))
