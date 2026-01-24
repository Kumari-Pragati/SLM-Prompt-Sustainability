import unittest
from mbpp_205_code import inversion_elements

class TestInversionElements(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(inversion_elements((1, 2, 3)), (~1, ~2, ~3))

    def test_empty(self):
        self.assertEqual(inversion_elements(()), ())

    def test_single_element(self):
        self.assertEqual(inversion_elements((1,)), (~1,))

    def test_negative(self):
        self.assertEqual(inversion_elements((-1, 2, 3)), (~(-1), ~2, ~3))

    def test_mixed(self):
        self.assertEqual(inversion_elements((-1, 2, 3, 4)), (~(-1), ~2, ~3, ~4))

    def test_large(self):
        self.assertEqual(inversion_elements((1, 2, 3, 4, 5, 6, 7, 8, 9, 10)), (~1, ~2, ~3, ~4, ~5, ~6, ~7, ~8, ~9, ~10))
