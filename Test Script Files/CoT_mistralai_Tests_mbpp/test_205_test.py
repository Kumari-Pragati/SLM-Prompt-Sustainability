import unittest
from mbpp_205_code import inversion_elements

class TestInversionElements(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(inversion_elements([]), ())

    def test_single_element(self):
        self.assertEqual(inversion_elements((1,)), (0,))
        self.assertEqual(inversion_elements((0,)), (1,))

    def test_positive_numbers(self):
        self.assertEqual(inversion_elements((1, 2, 3)), (0, 1, 2))
        self.assertEqual(inversion_elements((10, 20, 30)), (9, 19, 29))

    def test_negative_numbers(self):
        self.assertEqual(inversion_elements((-1, -2, -3)), (1, 2, 3))
        self.assertEqual(inversion_elements((-10, -20, -30)), (19, 10, 3))

    def test_mixed_numbers(self):
        self.assertEqual(inversion_elements((1, -2, 3, -4)), (0, 2, 3, 1))
        self.assertEqual(inversion_elements((-1, 2, -3, 4)), (1, 0, 3, 2))

    def test_duplicate_elements(self):
        self.assertEqual(inversion_elements((1, 1, 2)), (0, 1, 1))
        self.assertEqual(inversion_elements((-1, -1, 2)), (1, 0, 2))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            inversion_elements(123)
        with self.assertRaises(TypeError):
            inversion_elements("abc")
