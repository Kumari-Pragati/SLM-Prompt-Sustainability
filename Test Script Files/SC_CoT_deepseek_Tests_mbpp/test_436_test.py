import unittest
from mbpp_436_code import neg_nos

class TestNegNos(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(neg_nos([1, -2, 3]), -2)

    def test_no_negative_numbers(self):
        self.assertIsNone(neg_nos([1, 2, 3]))

    def test_empty_list(self):
        self.assertIsNone(neg_nos([]))

    def test_single_negative_number(self):
        self.assertEqual(neg_nos([-1]), -1)

    def test_negative_numbers_in_middle(self):
        self.assertEqual(neg_nos([1, -2, 3, -4, 5]), -2)

    def test_negative_numbers_at_end(self):
        self.assertEqual(neg_nos([1, 2, 3, -4]), -4)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            neg_nos("not a list")
