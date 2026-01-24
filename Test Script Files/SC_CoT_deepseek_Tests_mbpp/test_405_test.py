import unittest
from mbpp_405_code import check_tuplex

class TestCheckTuplex(unittest.TestCase):
    
    def test_typical_case(self):
        self.assertTrue(check_tuplex((1, 2, 3), (1, 2)))

    def test_edge_case(self):
        self.assertFalse(check_tuplex((1, 2, 3), (4, 5)))

    def test_empty_tuples(self):
        self.assertFalse(check_tuplex((), ()))

    def test_single_element_tuples(self):
        self.assertFalse(check_tuplex((1,), (1,)))

    def test_nested_tuples(self):
        self.assertFalse(check_tuplex(((1, 2), (3, 4)), (1, 2)))

    def test_invalid_input_tuplex(self):
        with self.assertRaises(TypeError):
            check_tuplex("not a tuple", (1, 2))

    def test_invalid_input_tuple1(self):
        with self.assertRaises(TypeError):
            check_tuplex((1, 2, 3), "not a tuple")
