import unittest
from mbpp_785_code import tuple_str_int

class TestTupleStrInt(unittest.TestCase):

    def test_empty_string(self):
        self.assertIsInstance(tuple_str_int(''), tuple, "Empty string should return an empty tuple.")

    def test_single_number(self):
        self.assertIsInstance(tuple_str_int('1'), tuple, "Single number should return a tuple with one element.")
        self.assertEqual(tuple_str_int('1'), (1,), "Single number should return a tuple with the number as the only element.")

    def test_multiple_numbers(self):
        self.assertIsInstance(tuple_str_int('1, 2, 3'), tuple, "Multiple numbers should return a tuple.")
        self.assertEqual(tuple_str_int('1, 2, 3'), (1, 2, 3), "Multiple numbers should return a tuple with the numbers in the given order.")

    def test_numbers_with_spaces(self):
        self.assertIsInstance(tuple_str_int('1 2 3'), tuple, "Numbers with spaces should return a tuple.")
        self.assertEqual(tuple_str_int('1 2 3'), (1, 2, 3), "Numbers with spaces should return a tuple with the numbers in the given order.")

    def test_numbers_with_commas_and_spaces(self):
        self.assertIsInstance(tuple_str_int('1, 2 ,3'), tuple, "Numbers with commas and spaces should return a tuple.")
        self.assertEqual(tuple_str_int('1, 2 ,3'), (1, 2, 3), "Numbers with commas and spaces should return a tuple with the numbers in the given order.")

    def test_numbers_with_parentheses(self):
        self.assertIsInstance(tuple_str_int('(1, 2, 3)'), tuple, "Numbers with parentheses should return a tuple.")
        self.assertEqual(tuple_str_int('(1, 2, 3)'), (1, 2, 3), "Numbers with parentheses should return a tuple with the numbers in the given order.")

    def test_numbers_with_parentheses_and_spaces(self):
        self.assertIsInstance(tuple_str_int('(1, 2 ,3)'), tuple, "Numbers with parentheses and spaces should return a tuple.")
        self.assertEqual(tuple_str_int('(1, 2 ,3)'), (1, 2, 3), "Numbers with parentheses and spaces should return a tuple with the numbers in the given order.")

    def test_numbers_with_parentheses_and_commas(self):
        self.assertIsInstance(tuple_str_int('(1, 2, 3, 4, 5)'), tuple, "Numbers with parentheses and commas should return a tuple.")
        self.assertEqual(tuple_str_int('(1, 2, 3, 4, 5)'), (1, 2, 3, 4, 5), "Numbers with parentheses and commas should return a tuple with the numbers in the given order.")

    def test_numbers_with_parentheses_and_commas_and_spaces(self):
        self.assertIsInstance(tuple_str_int('(1, 2 ,3, 4, 5)'), tuple, "Numbers with parentheses, commas, and spaces should return a tuple.")
        self.assertEqual(tuple_str_int('(1, 2 ,3, 4, 5)'), (1, 2, 3, 4, 5), "Numbers with parentheses, commas, and spaces should return a tuple with the numbers in the given order.")

    def test_numbers_with_ellipsis(self):
        self.assertIsInstance(tuple_str_int('1...3'), tuple, "Numbers with ellipsis should return a tuple.")
        self.assertEqual(tuple_str_int('1...3'), (1, 2, 3), "Numbers