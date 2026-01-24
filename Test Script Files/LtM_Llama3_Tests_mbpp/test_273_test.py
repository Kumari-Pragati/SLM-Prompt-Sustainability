import unittest
from mbpp_273_code import substract_elements

class TestSubstractElements(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(substract_elements((1, 2), (3, 4)), (-2, -2))

    def test_empty_input(self):
        with self.assertRaises(TypeError):
            substract_elements([], (1, 2))

    def test_single_element(self):
        self.assertEqual(substract_elements((1,), (2,)), (-1,))
        self.assertEqual(substract_elements((1, 2), ()), (1, 2))

    def test_negative_numbers(self):
        self.assertEqual(substract_elements((-1, 2), (3, -4)), (-4, 6))

    def test_large_numbers(self):
        self.assertEqual(substract_elements((1000, 2000), (3000, 4000)), (-1000, -1000))

    def test_mixed_signs(self):
        self.assertEqual(substract_elements((1, -2), (3, 4)), (-2, 2))
