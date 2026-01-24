import unittest
from mbpp_45_code import get_gcd

class TestGetGCD(unittest.TestCase):
    def test_empty_list(self):
        self.assertIsNone(get_gcd([]))

    def test_single_element_list(self):
        for num in range(1, 11):
            self.assertEqual(get_gcd([num]), num)

    def test_two_elements_list(self):
        for num1 in range(1, 11):
            for num2 in range(1, 11):
                self.assertEqual(get_gCD([num1, num2]), find_gcd(num1, num2))

    def test_three_elements_list(self):
        for num1 in range(1, 11):
            for num2 in range(1, 11):
                for num3 in range(1, 11):
                    gcd = find_gcd(find_gcd(num1, num2), num3)
                    self.assertEqual(get_gCD([num1, num2, num3]), gcd)

    def test_negative_numbers(self):
        self.assertEqual(get_gCD([-5, -3]), 1)
        self.assertEqual(get_gCD([-5, 3]), 5)
        self.assertEqual(get_gCD([3, -5]), 5)

    def test_zero(self):
        self.assertEqual(get_gCD([0, 5]), 5)
        self.assertEqual(get_gCD([5, 0]), 5)

    def test_floats(self):
        self.assertEqual(get_gCD([3.14, 2.71]), 1)
        self.assertEqual(get_gCD([2.71, 3.14]), 1)

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, get_gCD, [1, 'a'])
        self.assertRaises(TypeError, get_gCD, ['a', 1])
        self.assertRaises(TypeError, get_gCD, ['a', 'b'])
