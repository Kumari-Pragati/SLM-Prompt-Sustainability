import unittest
from mbpp_278_code import count_first_elements

class TestCountFirstElements(unittest.TestCase):

    def test_empty_list(self):
        self.assertIsInstance(count_first_elements([]), TypeError)

    def test_single_element(self):
        self.assertEqual(count_first_elements([1]), 0)

    def test_single_non_tuple_element(self):
        self.assertEqual(count_first_elements([(1, 2), 3]), 0)

    def test_single_tuple_element(self):
        self.assertIsInstance(count_first_elements([(1, 2)]), TypeError)

    def test_multiple_elements(self):
        self.assertEqual(count_first_elements([1, (1, 2), 3]), 0)

    def test_multiple_non_tuple_elements(self):
        self.assertEqual(count_first_elements([1, 2, 3]), 0)

    def test_multiple_tuple_elements(self):
        self.assertIsInstance(count_first_elements([(1, 2), (3, 4)]), TypeError)
