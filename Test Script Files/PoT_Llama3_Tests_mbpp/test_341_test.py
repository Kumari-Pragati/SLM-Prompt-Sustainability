import unittest
from mbpp_341_code import set_to_tuple

class TestSetToTuple(unittest.TestCase):
    def test_typical(self):
        self.assertEqual(set_to_tuple({1, 2, 3}), (1, 2, 3))
        self.assertEqual(set_to_tuple({'a', 'b', 'c'}), ('a', 'b', 'c'))
        self.assertEqual(set_to_tuple({5, 2, 1}), (1, 2, 5))

    def test_empty(self):
        self.assertEqual(set_to_tuple(set()), ())

    def test_single_element(self):
        self.assertEqual(set_to_tuple({4}), (4,))

    def test_duplicates(self):
        self.assertEqual(set_to_tuple({1, 1, 2, 2}), (1, 2))

    def test_negative(self):
        self.assertEqual(set_to_tuple({-1, 0, 1}), (-1, 0, 1))

    def test_mixed(self):
        self.assertEqual(set_to_tuple({1, 'a', 2, 'b'}), ('a', 'b', 1, 2))
