import unittest
from mbpp_106_code import add_lists

class TestAddLists(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(add_lists([1, 2, 3], (4, 5, 6)), (4, 5, 6, 1, 2, 3))

    def test_empty_lists_and_tuples(self):
        self.assertEqual(add_lists([], ()), ())

    def test_single_element_lists_and_tuples(self):
        self.assertEqual(add_lists([1], (2,)), (2, 1))

    def test_large_lists_and_tuples(self):
        self.assertEqual(add_lists(list(range(1, 101)), tuple(range(101, 201))), 
                         tuple(range(101, 201)) + list(range(1, 101)))

    def test_negative_numbers(self):
        self.assertEqual(add_lists([-1, -2, -3], (-4, -5, -6)), 
                         (-4, -5, -6, -1, -2, -3))

    def test_mixed_positive_and_negative_numbers(self):
        self.assertEqual(add_lists([1, -1, 2, -2], (3, -3, 4, -4)), 
                         (3, -3, 4, -4, 1, -1, 2, -2))
