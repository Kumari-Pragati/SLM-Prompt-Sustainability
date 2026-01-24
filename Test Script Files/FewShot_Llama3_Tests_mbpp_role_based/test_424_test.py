import unittest
from mbpp_424_code import extract_rear

class TestExtractRear(unittest.TestCase):
    def test_single_sub_element(self):
        test_tuple = (1, 2, 3)
        expected_output = [3]
        self.assertEqual(extract_rear(test_tuple), expected_output)

    def test_multiple_sub_elements(self):
        test_tuple = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
        expected_output = [3, 6, 9]
        self.assertEqual(extract_rear(test_tuple), expected_output)

    def test_empty_sub_elements(self):
        test_tuple = ()
        expected_output = []
        self.assertEqual(extract_rear(test_tuple), expected_output)

    def test_non_tuple_input(self):
        test_input = "test"
        with self.assertRaises(TypeError):
            extract_rear(test_input)
