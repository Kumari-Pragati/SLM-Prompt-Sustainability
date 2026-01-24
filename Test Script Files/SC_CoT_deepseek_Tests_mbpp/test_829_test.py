import unittest
from mbpp_829_code import second_frequent

class TestSecondFrequent(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(second_frequent([1, 2, 2, 3, 3, 3]), 2)

    def test_single_element(self):
        self.assertEqual(second_frequent([1]), None)

    def test_empty_list(self):
        self.assertEqual(second_frequent([]), None)

    def test_all_same_elements(self):
        self.assertEqual(second_frequent([1, 1, 1, 1]), None)

    def test_second_most_frequent(self):
        self.assertEqual(second_frequent([1, 2, 2, 3, 3]), 2)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            second_frequent("12345")
