import unittest
from mbpp_672_code import max_of_three

class TestMaxOfThree(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(max_of_three(10, 20, 15), 20)

    def test_num1_greater_than_num2_and_num3(self):
        self.assertEqual(max_of_three(30, 20, 10), 30)

    def test_num2_greater_than_num1_and_num3(self):
        self.assertEqual(max_of_three(10, 20, 15), 20)

    def test_num3_greater_than_num1_and_num2(self):
        self.assertEqual(max_of_three(10, 20, 30), 30)

    def test_equal_numbers(self):
        self.assertEqual(max_of_three(20, 20, 20), 20)

    def test_negative_numbers(self):
        self.assertEqual(max_of_three(-10, -20, -15), -10)

    def test_negative_and_positive_numbers(self):
        self.assertEqual(max_of_three(-10, 20, 15), 20)

    def test_zero(self):
        self.assertEqual(max_of_three(0, -20, 15), 15)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            max_of_three("10", 20, 15)
