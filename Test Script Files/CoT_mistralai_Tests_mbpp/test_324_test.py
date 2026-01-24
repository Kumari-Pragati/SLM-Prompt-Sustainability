import unittest
from mbpp_324_code import sum_of_alternates

class TestSumOfAlternates(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(sum_of_alternates([]), (0, 0))

    def test_single_element(self):
        for num in range(10):
            self.assertEqual(sum_of_alternates([num]), ((num, 0)))

    def test_even_length_list(self):
        for num1 in range(10):
            for num2 in range(10):
                self.assertEqual(sum_of_alternates([num1, num2]), ((num1, num2)))

    def test_odd_length_list(self):
        for num1 in range(10):
            for num2 in range(10):
                for num3 in range(10):
                    self.assertEqual(sum_of_alternates([num1, num2, num3]), ((num1 + num3, num2)))

    def test_negative_numbers(self):
        for num1 in range(-10, 0):
            for num2 in range(-10, 0):
                self.assertEqual(sum_of_alternates([num1, num2]), ((num1 + num2, 0)))

    def test_mixed_signs(self):
        for num1 in range(-10, 10):
            for num2 in range(-10, 10):
                self.assertEqual(sum_of_alternates([num1, num2]), ((num1 + num2, 0)))

    def test_invalid_input(self):
        self.assertRaises(TypeError, sum_of_alternates, [1, 2, 'a'])
        self.assertRaises(TypeError, sum_of_alternates, [1, 2, 3.14])
