import unittest
from mbpp_470_code import add_pairwise

class TestAddPairwise(unittest.TestCase):

    def test_empty_list(self):
        self.assertRaises(TypeError, add_pairwise, ())

    def test_single_element_list(self):
        self.assertRaises(TypeError, add_pairwise, (1,))

    def test_single_pair(self):
        self.assertEqual(add_pairwise((1, 2)), (3,))

    def test_pairwise_addition(self):
        self.assertEqual(add_pairwise((1, 2, 3, 4)), (3, 5, 6, 7))

    def test_negative_numbers(self):
        self.assertEqual(add_pairwise((-1, 2, -3, 4)), (1, 4, -2, 1))

    def test_mixed_types(self):
        self.assertRaises(TypeError, add_pairwise, ((1, 'a'), (2, 'b')))

    def test_list_with_non_iterable(self):
        self.assertRaises(TypeError, add_pairwise, ((1,), (2, 3)))
