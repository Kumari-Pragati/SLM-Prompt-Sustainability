import unittest
from mbpp_278_code import count_first_elements

class TestCountFirstElements(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(count_first_elements([]), 0)

    def test_single_element(self):
        self.assertEqual(count_first_elements([1]), 0)
        self.assertEqual(count_first_elements([(1, 2)]), 0)
        self.assertEqual(count_first_elements([(1, 2), 1]), 0)

    def test_multiple_elements(self):
        self.assertEqual(count_first_elements([1, 2, 3]), 0)
        self.assertEqual(count_first_elements([(1, 2), 1, 2, 3]), 1)
        self.assertEqual(count_first_elements([(1, 2), (3, 4), 1, 2, 3]), 0)

    def test_list_of_tuples(self):
        self.assertEqual(count_first_elements([(1, 2), (3, 4)]), 0)
        self.assertEqual(count_first_elements([(1, 2), (3, 4), (5, 6)]), 0)
        self.assertEqual(count_first_elements([(1, 2), (3, 4), (5, 6), (1, 2)]), 0)

    def test_list_of_tuples_and_numbers(self):
        self.assertEqual(count_first_elements([(1, 2), 3, (4, 5)]), 0)
        self.assertEqual(count_first_elements([(1, 2), 3, (4, 5), (1, 2)]), 0)
        self.assertEqual(count_first_elements([(1, 2), 3, (4, 5), 1, (2, 3)]), 1)

    def test_list_of_only_tuples(self):
        self.assertEqual(count_first_elements([(1, 2), (3, 4), (5, 6)]), 0)

    def test_list_with_nested_tuples(self):
        self.assertEqual(count_first_elements([(1, (2, 3)), (4, 5)]), 0)
        self.assertEqual(count_first_elements([(1, (2, 3)), (4, 5), (1, (2, 3))]), 0)
        self.assertEqual(count_first_elements([(1, (2, 3)), (4, 5), (1, (2, 3)), (1, (2, 3))]), 0)
