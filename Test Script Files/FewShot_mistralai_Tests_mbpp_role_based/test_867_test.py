import unittest
from mbpp_867_code import min_Num

class TestMinNum(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(min_Num([]), 2)

    def test_single_odd_element(self):
        self.assertEqual(min_Num([1]), 1)

    def test_single_even_element(self):
        self.assertEqual(min_Num([2]), 2)

    def test_all_odd_elements(self):
        self.assertEqual(min_Num([1, 3, 5]), 1)

    def test_all_even_elements(self):
        self.assertEqual(min_Num([2, 4, 6]), 2)

    def test_mixed_odd_and_even_elements(self):
        self.assertEqual(min_Num([1, 2, 3, 4, 5]), 1)

    def test_invalid_input_list(self):
        with self.assertRaises(TypeError):
            min_Num('string', 5)

    def test_invalid_input_n(self):
        with self.assertRaises(TypeError):
            min_Num([1, 2, 3], 'string')
