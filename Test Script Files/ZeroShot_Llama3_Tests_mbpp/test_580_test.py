import unittest
from mbpp_580_code import extract_even

class TestExtractEven(unittest.TestCase):
    def test_extract_even(self):
        self.assertEqual(extract_even((1, 2, 3, 4, 5)), (2, 4))
        self.assertEqual(extract_even((1, 2, 3, 4, 5, (1, 2, 3, 4, 5))), (2, 4, (2, 4)))
        self.assertEqual(extract_even((1, 2, 3, 4, 5, (1, 2, 3, 4, 5), (6, 7, 8, 9, 10))), (2, 4, (2, 4), (4, 6, 8)))
        self.assertEqual(extract_even(()), ())
        self.assertEqual(extract_even((1,)), ())

    def test_extract_even_with_empty_tuple(self):
        self.assertEqual(extract_even(()), ())

    def test_extract_even_with_single_element(self):
        self.assertEqual(extract_even((1,)), (1,))
