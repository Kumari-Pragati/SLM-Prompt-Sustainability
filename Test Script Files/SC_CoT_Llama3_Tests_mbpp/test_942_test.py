import unittest
from mbpp_942_code import check_element

class TestCheckElement(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(check_element((1, 2, 3), [1, 2]))

    def test_edge_case(self):
        self.assertTrue(check_element((1, 2, 3), [3]))

    def test_edge_case2(self):
        self.assertFalse(check_element((1, 2, 3), [4]))

    def test_edge_case3(self):
        self.assertFalse(check_element((1, 2, 3), []))

    def test_edge_case4(self):
        self.assertFalse(check_element((), [1]))

    def test_edge_case5(self):
        self.assertFalse(check_element([1], [1]))

    def test_edge_case6(self):
        self.assertTrue(check_element((1, 2, 3), [1, 2, 3]))

    def test_edge_case7(self):
        self.assertFalse(check_element((1, 2, 3), [1, 4]))

    def test_edge_case8(self):
        self.assertFalse(check_element((1, 2, 3), [2, 4]))

    def test_edge_case9(self):
        self.assertFalse(check_element((1, 2, 3), [3, 4]))

    def test_edge_case10(self):
        self.assertFalse(check_element((1, 2, 3), [1, 2, 4]))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            check_element(1, [1, 2])
