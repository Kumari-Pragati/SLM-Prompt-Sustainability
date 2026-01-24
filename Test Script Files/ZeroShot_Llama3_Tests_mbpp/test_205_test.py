import unittest
from mbpp_205_code import inversion_elements

class TestInversionElements(unittest.TestCase):

    def test_inversion_elements(self):
        self.assertEqual(inversion_elements((1, 0, 1)), (~1, ~0, ~1))
        self.assertEqual(inversion_elements((0, 1, 0)), (~0, ~1, ~0))
        self.assertEqual(inversion_elements((-1, 0, 1)), (~(-1), ~0, ~1))
        self.assertEqual(inversion_elements((0, 0, 0)), (~0, ~0, ~0))
        self.assertEqual(inversion_elements((-1, -1, -1)), (~(-1), ~(-1), ~(-1)))
        self.assertEqual(inversion_elements((1, 1, 1)), (~1, ~1, ~1))
        self.assertEqual(inversion_elements((-1, 1, 0)), (~(-1), ~1, ~0))
        self.assertEqual(inversion_elements((0, 0, 1)), (~0, ~0, ~1))
        self.assertEqual(inversion_elements((1, 0, 1)), (~1, ~0, ~1))

    def test_inversion_elements_empty(self):
        self.assertEqual(inversion_elements(()), ())

    def test_inversion_elements_single(self):
        self.assertEqual(inversion_elements((1,)), (~1,))

    def test_inversion_elements_negative(self):
        self.assertEqual(inversion_elements((-1,)), (~(-1),))
