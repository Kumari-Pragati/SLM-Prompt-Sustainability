import unittest
from mbpp_205_code import inversion_elements

class TestInversionElements(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(inversion_elements(()), ())

    def test_single_element(self):
        for bit in (0, 1):
            self.assertEqual(inversion_elements((bit,)), (~bit,))

    def test_positive_integer_list(self):
        for num in range(10):
            self.assertEqual(inversion_elements((1 << num,)), ((1 << num) ^ (1 << num),))

    def test_negative_integer_list(self):
        for num in range(10, 0, -1):
            self.assertEqual(inversion_elements((-1 << num,)), ((-1 << num) ^ ((1 << num) - 1),))

    def test_mixed_bit_list(self):
        test_list = (0, 1, -1, -2, 3, -4, 5, -8, 9)
        expected_list = (1, 0, ~(-1), ~(-2), ~(3), ~(-4), 5, ~(-8), ~(9))
        self.assertEqual(inversion_elements(test_list), tuple(expected_list))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            inversion_elements(123)
        with self.assertRaises(TypeError):
            inversion_elements([1, 2, 3])
