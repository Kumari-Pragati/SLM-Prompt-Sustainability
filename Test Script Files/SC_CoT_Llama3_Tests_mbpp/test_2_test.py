import unittest
from mbpp_2_code import similar_elements

class TestSimilarElements(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(similar_elements((1, 2, 3, 4), (2, 3, 4, 5)), (2, 3, 4))

    def test_edge_case_empty_input(self):
        self.assertEqual(similar_elements((), (1, 2, 3)), ())

    def test_edge_case_single_input(self):
        self.assertEqual(similar_elements((1, 2, 3), ()), ())

    def test_edge_case_empty_input2(self):
        self.assertEqual(similar_elements((1, 2, 3, 4), ()), ())

    def test_edge_case_single_input2(self):
        self.assertEqual(similar_elements((), (1, 2, 3, 4)), ())

    def test_edge_case_duplicates(self):
        self.assertEqual(similar_elements((1, 2, 2, 3), (2, 2, 3, 4)), (2, 2, 3))

    def test_edge_case_duplicates2(self):
        self.assertEqual(similar_elements((1, 2, 3, 4), (1, 2, 2, 3)), (1, 2, 2, 3))

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            similar_elements("hello", (1, 2, 3))

    def test_invalid_input_type2(self):
        with self.assertRaises(TypeError):
            similar_elements((1, 2, 3), "hello")

    def test_invalid_input_type3(self):
        with self.assertRaises(TypeError):
            similar_elements("hello", "world")

    def test_invalid_input_type4(self):
        with self.assertRaises(TypeError):
            similar_elements([1, 2, 3], (1, 2, 3))

    def test_invalid_input_type5(self):
        with self.assertRaises(TypeError):
            similar_elements((1, 2, 3), [1, 2, 3])
