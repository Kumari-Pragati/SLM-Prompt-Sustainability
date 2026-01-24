import unittest
from mbpp_439_code import multiple_to_single

class TestMultipleToSingle(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(multiple_to_single([1, 2, 3, 4, 5]), 12345)
        self.assertEqual(multiple_to_single([10, 20, 30, 40, 50]), 123450)
        self.assertEqual(multiple_to_single([100, 200, 300, 400, 500]), 1234500)

    def test_single_number(self):
        self.assertEqual(multiple_to_single([1]), 1)
        self.assertEqual(multiple_to_single([10]), 10)
        self.assertEqual(multiple_to_single([100]), 100)

    def test_empty_list(self):
        self.assertEqual(multiple_to_single([]), 0)

    def test_negative_numbers(self):
        self.assertEqual(multiple_to_single([-1, -2, -3, -4, -5]), 12345)
        self.assertEqual(multiple_to_single([-10, -20, -30, -40, -50]), 123450)
        self.assertEqual(multiple_to_string([-100, -200, -300, -400, -500]), 1234500)

    def test_mixed_numbers(self):
        self.assertEqual(multiple_to_single([1, -2, 3, -4, 5]), 1-2345)
        self.assertEqual(multiple_to_single([10, -20, 30, -40, 50]), 1-23450)
        self.assertEqual(multiple_to_single([100, -200, 300, -400, 500]), 1-234500)

    def test_non_integer_input(self):
        self.assertRaises(TypeError, multiple_to_single, [1.5, 2, 3])
        self.assertRaises(TypeError, multiple_to_single, [1, '2', 3])
        self.assertRaises(TypeError, multiple_to_single, [1, 2, '3'])
