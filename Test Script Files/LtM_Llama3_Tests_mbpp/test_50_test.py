import unittest
from mbpp_50_code import min_length_list

class TestMinLengthList(unittest.TestCase):
    def test_simple_valid_input(self):
        self.assertEqual(min_length_list([[1, 2], [3, 4], [5, 6]]), (2, [1, 2]))

    def test_empty_input(self):
        self.assertEqual(min_length_list([]), (0, None))

    def test_single_element_input(self):
        self.assertEqual(min_length_list([[1, 2]]), (1, [1, 2]))

    def test_multiple_elements_input(self):
        self.assertEqual(min_length_list([[1, 2], [3, 4], [5, 6]]), (2, [1, 2]))

    def test_input_with_duplicates(self):
        self.assertEqual(min_length_list([[1, 2], [1, 2], [3, 4]]), (1, [1, 2]))

    def test_input_with_empty_sublists(self):
        self.assertEqual(min_length_list([[1, 2], [], [3, 4]]), (1, [1, 2]))

    def test_input_with_sublists_of_different_lengths(self):
        self.assertEqual(min_length_list([[1, 2], [3, 4, 5], [6]]), (1, [6]))
