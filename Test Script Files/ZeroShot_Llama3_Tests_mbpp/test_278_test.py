import unittest
from mbpp_278_code import count_first_elements

class TestCountFirstElements(unittest.TestCase):

    def test_count_first_elements(self):
        self.assertEqual(count_first_elements((1, 2, 3)), 0)
        self.assertEqual(count_first_elements((1, (2, 3), 4)), 1)
        self.assertEqual(count_first_elements((1, (2, 3), 4, 5)), 1)
        self.assertEqual(count_first_elements((1, 2, 3, 4, 5)), 0)
        self.assertEqual(count_first_elements((1, (2, 3), (4, 5), 6)), 1)
        self.assertEqual(count_first_elements((1, 2, 3, (4, 5), 6)), 2)
        self.assertEqual(count_first_elements((1, 2, 3, 4, 5, 6)), 0)

    def test_count_first_elements_empty(self):
        self.assertEqual(count_first_elements(()), 0)

    def test_count_first_elements_single_element(self):
        self.assertEqual(count_first_elements((1,)), 0)

    def test_count_first_elements_single_tuple(self):
        self.assertEqual(count_first_elements((1, (2, 3))), 1)

    def test_count_first_elements_multiple_tuples(self):
        self.assertEqual(count_first_elements((1, (2, 3), (4, 5), (6, 7))), 1)
