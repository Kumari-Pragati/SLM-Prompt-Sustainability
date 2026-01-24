import unittest
from mbpp_424_code import extract_rear

class TestExtractRear(unittest.TestCase):
    def test_typical_input(self):
        test_tuple = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
        self.assertEqual(extract_rear(test_tuple), [(3,), (6,), (9,)])

    def test_edge_case_empty(self):
        test_tuple = ()
        self.assertEqual(extract_rear(test_tuple), [])

    def test_edge_case_single_element(self):
        test_tuple = ((1, 2, 3),)
        self.assertEqual(extract_rear(test_tuple), [(3,)])

    def test_edge_case_single_element_empty(self):
        test_tuple = ((),)
        self.assertEqual(extract_rear(test_tuple), [])

    def test_edge_case_multiple_empty(self):
        test_tuple = ((), (), ())
        self.assertEqual(extract_rear(test_tuple), [])

    def test_invalid_input_non_tuple(self):
        with self.assertRaises(TypeError):
            extract_rear("Invalid input")

    def test_invalid_input_non_iterable(self):
        with self.assertRaises(TypeError):
            extract_rear(123)

    def test_invalid_input_non_sequence(self):
        with self.assertRaises(TypeError):
            extract_rear({"Invalid input"})
