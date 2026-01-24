import unittest
from mbpp_205_code import inversion_elements

class TestInversionElements(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(inversion_elements((1, 2, 3)), (~1, ~2, ~3))

    def test_negative_numbers(self):
        self.assertEqual(inversion_elements((-1, -2, -3)), (~(-1), ~(-2), ~(-3)))

    def test_empty_list(self):
        self.assertEqual(inversion_elements([]), ())

    def test_single_element(self):
        self.assertEqual(inversion_elements((1,)), (~1,))

    def test_mixed_numbers(self):
        self.assertEqual(inversion_elements((1, -2, 3)), (~1, ~(-2), ~3))
