import unittest
from mbpp_810_code import Counter
from 810_code import count_variable

class TestCountVariable(unittest.TestCase):

    def test_typical_case(self):
        result = count_variable(1, 2, 3, 4)
        self.assertListEqual(result, [1, 2, 3, 4])

    def test_single_element(self):
        result = count_variable(5, 0, 0, 0)
        self.assertListEqual(result, [5])

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            count_variable(0, 0, 0, 0)

    def test_negative_elements(self):
        result = count_variable(-1, -2, -3, -4)
        self.assertListEqual(result, [-1, -2, -3, -4])

    def test_mixed_types(self):
        with self.assertRaises(TypeError):
            count_variable(1, 2.5, 3, "d")

    def test_duplicate_elements(self):
        result = count_variable(1, 2, 3, 3)
        self.assertListEqual(result, [1, 2, 3, 3])
