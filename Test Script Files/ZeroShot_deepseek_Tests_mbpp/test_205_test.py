import unittest
from mbpp_205_code import inversion_elements

class TestInversionElements(unittest.TestCase):

    def test_inversion_elements(self):
        self.assertEqual(inversion_elements((1, 2, 3)), (~1, ~2, ~3))
        self.assertEqual(inversion_elements((4, 5, 6)), (~4, ~5, ~6))
        self.assertEqual(inversion_elements(()), ())
        self.assertEqual(inversion_elements((7,)), (~7,))
        self.assertEqual(inversion_elements((-1, -2, -3)), (~-1, ~-2, ~-3))
