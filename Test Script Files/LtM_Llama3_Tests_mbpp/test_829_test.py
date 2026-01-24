import unittest
from mbpp_829_code import second_frequent

class TestSecondFrequent(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(second_frequent([]), None)

    def test_single_element_input(self):
        self.assertEqual(second_frequent([1]), 1)

    def test_multiple_elements_input(self):
        self.assertEqual(second_frequent([1, 2, 2, 3, 3, 3]), 2)

    def test_edge_case_input(self):
        self.assertEqual(second_frequent([1, 1, 1, 1, 1]), 1)

    def test_edge_case_input2(self):
        self.assertEqual(second_frequent([1, 2, 3, 4, 5]), 2)

    def test_edge_case_input3(self):
        self.assertEqual(second_frequent([1, 1, 2, 2, 3, 3, 4, 4, 5, 5]), 2)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            second_frequent('hello')
