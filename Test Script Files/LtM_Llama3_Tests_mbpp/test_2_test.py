import unittest
from mbpp_2_code import similar_elements

class TestSimilarElements(unittest.TestCase):
    def test_empty_inputs(self):
        self.assertEqual(similar_elements((), ()), ())
    def test_single_element(self):
        self.assertEqual(similar_elements((1,), (1,)), (1,))
    def test_multiple_elements(self):
        self.assertEqual(similar_elements((1, 2, 3), (2, 3, 4)), (2, 3))
    def test_empty_second_input(self):
        self.assertEqual(similar_elements((1, 2, 3), ()), ())
    def test_empty_first_input(self):
        self.assertEqual(similar_elements((), (1, 2, 3)), ())
    def test_duplicates(self):
        self.assertEqual(similar_elements((1, 1, 2), (1, 2, 2)), (1, 2))
    def test_order_matters(self):
        self.assertEqual(similar_elements((1, 2), (2, 1)), (1, 2))
