import unittest
from mbpp_579_code import find_dissimilar

class TestFindDissimilar(unittest.TestCase):
    def test_empty_inputs(self):
        self.assertEqual(find_dissimilar((), ()), ())
    def test_single_element(self):
        self.assertEqual(find_dissimilar((1,), ()), (1,))
    def test_empty_input_with_single_element(self):
        self.assertEqual(find_dissimilar((1,), ()), (1,))
    def test_empty_input_with_multiple_elements(self):
        self.assertEqual(find_dissimilar((1,2,3), ()), (1,2,3))
    def test_multiple_elements(self):
        self.assertEqual(find_dissimilar((1,2,3), (2,3,4)), (1,4))
    def test_duplicates(self):
        self.assertEqual(find_dissimilar((1,1,2), (1,2,2)), (1,2))
    def test_duplicates_in_second_input(self):
        self.assertEqual(find_dissimilar((1,2,3), (1,1,2)), (3))
    def test_duplicates_in_both_inputs(self):
        self.assertEqual(find_dissimilar((1,1,2,2), (1,1,2,2)), ())
