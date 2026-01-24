import unittest
from mbpp_580_code import extract_even

class TestExtractEven(unittest.TestCase):

    def test_even_numbers(self):
        self.assertEqual(extract_even((1, 2, 3, 4, 5, 6)), (2, 4, 6))

    def test_nested_tuples(self):
        self.assertEqual(extract_even(((1, 2), (3, 4), (5, 6))), ((2,), (4,), (6,)))

    def test_mixed_types(self):
        self.assertEqual(extract_even((1, '2', 3.5, 4, [5], {6: 'six'})), (4,))

    def test_empty_tuple(self):
        self.assertEqual(extract_even(()), ())

    def test_all_odd_numbers(self):
        self.assertEqual(extract_even((1, 3, 5, 7, 9)), ())
