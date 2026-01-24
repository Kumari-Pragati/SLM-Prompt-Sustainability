import unittest
from mbpp_351_code import first_Element

class TestFirstElement(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(first_Element([], 0, 1), -1)

    def test_single_element(self):
        self.assertEqual(first_Element([1], 1, 1), 1)

    def test_multiple_elements(self):
        self.assertEqual(first_Element([1, 2, 3, 2, 1], 5, 2), 2)

    def test_non_existent_element(self):
        self.assertEqual(first_Element([1, 2, 3], 3, 4), -1)

    def test_element_count_greater_than_k(self):
        self.assertEqual(first_Element([1, 1, 2, 2, 3], 5, 2), -1)

    def test_k_greater_than_n(self):
        self.assertEqual(first_Element([1, 2], 2, 3), -1)
