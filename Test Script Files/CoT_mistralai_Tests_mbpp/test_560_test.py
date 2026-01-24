import unittest
from mbpp_560_code import union_elements

class TestUnionElements(unittest.TestCase):

    def test_empty_tuples(self):
        self.assertCountEqual(union_elements((), ()), ())

    def test_single_element_tuples(self):
        self.assertCountEqual(union_elements((1,), (2,)), (1, 2))
        self.assertCountEqual(union_elements((2,), (1,)), (1, 2))

    def test_identical_tuples(self):
        self.assertCountEqual(union_elements((1, 2, 3), (1, 2, 3)), (1, 2, 3))

    def test_different_tuples(self):
        self.assertCountEqual(union_elements((1, 2, 3), (3, 4, 5)), (1, 2, 3, 4, 5))
        self.assertCountEqual(union_elements((3, 4, 5), (1, 2, 3)), (1, 2, 3, 4, 5))

    def test_duplicate_elements(self):
        self.assertCountEqual(union_elements((1, 1, 2), (2, 3)), (1, 2, 3))
        self.assertCountEqual(union_elements((2, 3), (1, 1, 2)), (1, 2, 3))

    def test_empty_tuple_and_single_element(self):
        self.assertCountEqual(union_elements((), (1,)), (1,))

    def test_single_element_and_empty_tuple(self):
        self.assertCountEqual(union_elements((1,), ()), (1,))

    def test_invalid_input_1(self):
        with self.assertRaises(TypeError):
            union_elements(1, 2)

    def test_invalid_input_2(self):
        with self.assertRaises(TypeError):
            union_elements([1, 2], [3, 4])
