import unittest
from mbpp_924_code import max_of_two

class TestMaxOfTwo(unittest.TestCase):

    # Test for simple / typical inputs
    def test_typical_inputs(self):
        self.assertEqual(max_of_two(5, 10), 10)
        self.assertEqual(max_of_two(0, 0), 0)
        self.assertEqual(max_of_two(-5, 3), 3)

    # Test for edge and boundary conditions
    def test_edge_conditions(self):
        self.assertEqual(max_of_two(0, -1), 0)
        self.assertEqual(max_of_two(float('-inf'), float('inf')), float('inf'))

    # Test for more complex or corner cases
    def test_complex_cases(self):
        self.assertEqual(max_of_two(float('nan'), float('nan')), float('nan'))
        self.assertEqual(max_of_two(float('inf'), float('-inf')), float('inf'))
