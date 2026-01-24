import unittest
from mbpp_384_code import frequency_Of_Smallest

class TestFrequencyOfSmallest(unittest.TestCase):

    # Test for simple / typical inputs
    def test_typical_inputs(self):
        self.assertEqual(frequency_Of_Smallest(5, [1, 2, 3, 2, 1]), 2)
        self.assertEqual(frequency_Of_Smallest(6, [1, 1, 1, 1, 1, 1]), 6)
        self.assertEqual(frequency_Of_Smallest(4, [4, 3, 2, 1]), 1)

    # Test for edge and boundary conditions
    def test_edge_conditions(self):
        self.assertEqual(frequency_Of_Smallest(1, [1]), 1)
        self.assertEqual(frequency_Of_Smallest(0, []), None)
        self.assertEqual(frequency_Of_Smallest(5, [10, 20, 30, 40, 50]), 1)

    # Test for more complex or corner cases
    def test_complex_cases(self):
        self.assertEqual(frequency_Of_Smallest(5, [1, 1, 2, 2, 3]), 2)
        self.assertEqual(frequency_Of_Smallest(5, [3, 2, 1, 1, 1]), 3)
        self.assertEqual(frequency_Of_Smallest(5, [1, 2, 3, 4, 5]), 1)
