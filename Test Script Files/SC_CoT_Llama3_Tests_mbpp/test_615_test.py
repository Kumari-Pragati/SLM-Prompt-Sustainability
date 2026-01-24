import unittest
from mbpp_615_code import average_tuple

class TestAverageTuple(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(average_tuple([[1, 2, 3], [4, 5, 6]]), [3.0, 5.0])

    def test_edge_case_empty_input(self):
        self.assertEqual(average_tuple([]), [])

    def test_edge_case_single_input(self):
        self.assertEqual(average_tuple([[1, 2, 3]]), [2.0])

    def test_edge_case_single_element_input(self):
        self.assertEqual(average_tuple([[1]]), [1.0])

    def test_edge_case_single_element_input_zero(self):
        self.assertEqual(average_tuple([[0]]), [0.0])

    def test_edge_case_single_element_input_negative(self):
        self.assertEqual(average_tuple([[-1]]), [-1.0])

    def test_edge_case_single_element_input_positive(self):
        self.assertEqual(average_tuple([[1]]), [1.0])

    def test_edge_case_single_element_input_half(self):
        self.assertEqual(average_tuple([[0.5]]), [0.5])

    def test_edge_case_single_element_input_half_negative(self):
        self.assertEqual(average_tuple([[-0.5]]), [-0.5])

    def test_edge_case_single_element_input_half_positive(self):
        self.assertEqual(average_tuple([[0.5]]), [0.5])

    def test_edge_case_single_element_input_half_zero(self):
        self.assertEqual(average_tuple([[0.0]]), [0.0])

    def test_edge_case_single_element_input_half_one(self):
        self.assertEqual(average_tuple([[0.5]]), [0.5])

    def test_edge_case_single_element_input_half_two(self):
        self.assertEqual(average_tuple([[0.5]]), [0.5])

    def test_edge_case_single_element_input_half_three(self):
        self.assertEqual(average_tuple([[0.5]]), [0.5])

    def test_edge_case_single_element_input_half_four(self):
        self.assertEqual(average_tuple([[0.5]]), [0.5])

    def test_edge_case_single_element_input_half_five(self):
        self.assertEqual(average_tuple([[0.5]]), [0.5])

    def test_edge_case_single_element_input_half_six(self):
        self.assertEqual(average_tuple([[0.5]]), [0.5])

    def test_edge_case_single_element_input_half_seven(self):
        self.assertEqual(average_tuple([[0.5]]), [0.5])

    def test_edge_case_single_element_input_half_eight(self):
        self.assertEqual(average_tuple([[0.5]]), [0.5])

    def test_edge_case_single_element_input_half_nine(self):
        self.assertEqual(average_tuple([[0.5]]), [0.5])

    def test_edge_case_single_element_input_half_ten(self):
        self.assertEqual(average_tuple([[0.5]]), [0.5])

    def test_edge_case_single_element_input_half_eleven(self):
        self.assertEqual(average_tuple([[0.5]]), [0.5])

    def test_edge_case_single_element_input_half_twelve(self):
        self.assertEqual(average_tuple([[0.5]]), [0.5])

    def test_edge_case_single_element_input_half_thirteen(self):
        self.assertEqual(average_tuple([[0.5]]), [0.5])

    def test_edge_case_single_element_input_half_fourteen(self):
        self.assertEqual(average_tuple([[0.5]]), [0.5])

    def test_edge_case_single_element_input_half_fifteen(self):
        self.assertEqual(average_tuple([[0.5]]), [0.5])

    def test_edge_case_single_element_input_half_sixteen(self):
        self.assertEqual(average_tuple([[0.5]]), [0.5])

    def test_edge_case_single_element_input_half_seventeen(self):
        self.assertEqual(average_tuple([[0.5]]), [0.5])

    def test_edge_case_single_element_input_half_eighteen(self):
        self.assertEqual(average_tuple([[0.5]]), [0.5])

    def test_edge_case_single_element_input_half_nineteen(self):
        self.assertEqual(average_tuple([[0.5]]), [0.5])

    def test_edge_case_single_element_input_half_twenty(self):
        self.assertEqual(average_tuple([[0.5]]), [0.5])

    def test_edge_case_single_element_input_half_twenty_one(self):
        self.assertEqual(average_tuple([[0.5]]), [0.5])

    def test_edge_case_single_element_input_half_twenty_two(self):
        self.assertEqual(average_tuple([[0.5]]), [0.5])

    def test_edge_case_single_element_input_half_twenty_three(self):
        self.assertEqual(average_tuple([[0.5]]), [0.5])

    def