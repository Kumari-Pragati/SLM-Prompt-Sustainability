import unittest
from mbpp_500_code import concatenate_elements

class TestConcatenateElements(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(concatenate_elements([1, 2, 3]), "1 2 3")

    def test_empty_list(self):
        self.assertEqual(concatenate_elements([]), "")

    def test_single_element(self):
        self.assertEqual(concatenate_elements([4]), "4")

    def test_list_with_spaces(self):
        self.assertEqual(concatenate_elements(["a", " ", "b"]), "a b")

    def test_list_with_numbers_and_strings(self):
        self.assertEqual(concatenate_elements([5, "x", 7, "y"]), "5 x 7 y")

    def test_list_with_none(self):
        self.assertEqual(concatenate_elements([None]), "None")

    def test_list_with_lists(self):
        self.assertEqual(concatenate_elements([[1], [2], [3]]), "1 2 3")
