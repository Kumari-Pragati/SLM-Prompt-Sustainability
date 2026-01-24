import unittest
from mbpp_439_code import multiple_to_single

class TestMultipleToSingle(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(multiple_to_single([1, 2, 3, 4]), 1234)
        self.assertEqual(multiple_to_single([0, 0, 0, 0]), 0)
        self.assertEqual(multiple_to_single([-1, -2, -3, -4]), 1234)

    def test_single_element(self):
        self.assertEqual(multiple_to_single([1]), 1)
        self.assertEqual(multiple_to_single([0]), 0)
        self.assertEqual(multiple_to_single([-1]), -1)

    def test_empty_list(self):
        self.assertEqual(multiple_to_single([]), 0)

    def test_mixed_types(self):
        self.assertRaises(TypeError, multiple_to_single, [1, 2, '3', 4])
        self.assertRaises(TypeError, multiple_to_single, [1, 2, 3.0, 4])
