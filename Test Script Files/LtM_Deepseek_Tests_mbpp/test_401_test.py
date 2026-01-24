import unittest
from mbpp_401_code import add_nested_tuples

class TestAddNestedTuples(unittest.TestCase):

    # Test for simple / typical inputs
    def test_simple_inputs(self):
        self.assertEqual(add_nested_tuples(((1, 2), (3, 4)), ((5, 6), (7, 8))), ((6, 8), (10, 12)))

    # Test for edge and boundary conditions
    def test_empty_inputs(self):
        self.assertEqual(add_nested_tuples((), ()), ())

    def test_single_element_inputs(self):
        self.assertEqual(add_nested_tuples(((1,),), ((2,),)), ((3,),))

    # Test for more complex or corner cases
    def test_different_length_inputs(self):
        self.assertEqual(add_nested_tuples(((1, 2), (3, 4)), ((5, 6),)), ((6, 8), (3, 4)))

    def test_large_numbers(self):
        self.assertEqual(add_nested_tuples(((1000000, 2000000), (3000000, 4000000)), ((5000000, 6000000), (7000000, 8000000))), ((16000000, 24000000), (10000000, 12000000)))
