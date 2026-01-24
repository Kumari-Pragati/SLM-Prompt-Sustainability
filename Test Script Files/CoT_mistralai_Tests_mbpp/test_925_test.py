import unittest
from mbpp_925_code import mutiple_tuple

class TestMutipleTuple(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(mutiple_tuple([]), 1)

    def test_single_element_list(self):
        for num in range(1, 11):
            self.assertEqual(mutiple_tuple([num]), num)

    def test_multiple_elements_list(self):
        for num1 in range(1, 11):
            for num2 in range(1, 11):
                self.assertEqual(mutiple_tuple([num1, num2]), num1 * num2)

    def test_negative_numbers(self):
        for num1 in range(-10, 0):
            for num2 in range(-10, 0):
                self.assertEqual(mutiple_tuple([num1, num2]), num1 * num2)

    def test_zero(self):
        self.assertEqual(mutiple_tuple([0]), 0)
        self.assertEqual(mutiple_tuple([0, 1]), 0)
        self.assertEqual(mutiple_tuple([1, 0]), 0)

    def test_floats(self):
        self.assertAlmostEqual(mutiple_tuple([1.5, 2.5]), 3.75)
        self.assertAlmostEqual(mutiple_tuple([-1.5, -2.5]), 3.75)

    def test_invalid_input(self):
        self.assertRaises(TypeError, mutiple_tuple, "not a list")
        self.assertRaises(TypeError, mutiple_tuple, [1, "two"])
