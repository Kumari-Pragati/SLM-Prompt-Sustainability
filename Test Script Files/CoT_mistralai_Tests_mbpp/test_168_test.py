import unittest
from mbpp_168_code import frequency

class TestFrequency(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(frequency([]), 0)

    def test_single_element(self):
        self.assertEqual(frequency([1]), 1)

    def test_multiple_elements(self):
        self.assertEqual(frequency([1, 1, 2, 1, 3, 1]), 4)

    def test_duplicate_elements(self):
        self.assertEqual(frequency([1, 1, 1, 2, 1, 1]), 5)

    def test_negative_number(self):
        self.assertEqual(frequency([-1, -1, 1]), 2)

    def test_non_integer_input(self):
        self.assertRaises(TypeError, lambda: frequency(["a", "b"], 1))

    def test_non_existent_element(self):
        self.assertEqual(frequency([1, 2, 3], 4), 0)
