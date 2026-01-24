import unittest
from mbpp_922_code import max_product

class TestMaxProduct(unittest.TestCase):

    def test_empty_list(self):
        self.assertIsNone(max_product([]))

    def test_single_element_list(self):
        for num in range(-10, 10):
            self.assertIsNone(max_product([num]))

    def test_two_elements_list(self):
        for num1 in range(-10, 10):
            for num2 in range(-10, 10):
                result = max_product([num1, num2])
                self.assertIsInstance(result, tuple)
                self.assertEqual(len(result), 2)
                self.assertAlmostEqual(result[0], max(num1, num2))
                self.assertAlmostEqual(result[1], min(num1, num2))

    def test_negative_numbers(self):
        for num1 in range(-10, 0):
            for num2 in range(-10, 0):
                result = max_product([num1, num2])
                self.assertIsInstance(result, tuple)
                self.assertEqual(len(result), 2)
                self.assertAlmostEqual(result[0], min(num1, num2))
                self.assertAlmostEqual(result[1], max(num1, num2))

    def test_positive_and_negative_numbers(self):
        for num1 in range(-10, 10):
            for num2 in range(-10, 10):
                if num1 > 0 and num2 > 0:
                    self.assertIsInstance(max_product([num1, num2]), tuple)
                    self.assertEqual(len(max_product([num1, num2])), 2)
                    self.assertAlmostEqual(max_product([num1, num2])[0], max(num1, num2))
                    self.assertAlmostEqual(max_product([num1, num2])[1], min(num1, num2))
                elif num1 < 0 and num2 < 0:
                    self.assertIsInstance(max_product([num1, num2]), tuple)
                    self.assertEqual(len(max_product([num1, num2])), 2)
                    self.assertAlmostEqual(max_product([num1, num2])[0], min(num1, num2))
                    self.assertAlmostEqual(max_product([num1, num2])[1], max(num1, num2))
                else:
                    self.assertIsNone(max_product([num1, num2]))
