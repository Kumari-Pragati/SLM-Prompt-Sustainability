import unittest
from mbpp_278_code import count_first_elements

class TestCountFirstElements(unittest.TestCase):
    def test_typical_use_case(self):
        test_tup = (1, 2, (3, 4), 5, 6)
        self.assertEqual(count_first_elements(test_tup), 3)

    def test_edge_case_empty_tuple(self):
        test_tup = ()
        self.assertEqual(count_first_elements(test_tup), 0)

    def test_edge_case_single_element_tuple(self):
        test_tup = (1,)
        self.assertEqual(count_first_elements(test_tup), 1)

    def test_edge_case_no_tuples(self):
        test_tup = (1, 2, 3, 4, 5)
        self.assertEqual(count_first_elements(test_tup), 5)

    def test_invalid_input_non_tuple(self):
        test_tup = "Invalid input"
        with self.assertRaises(TypeError):
            count_first_elements(test_tup)
