import unittest
from mbpp_489_code import frequency_Of_Largest

class TestFrequencyOfLargest(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(frequency_Of_Largest(5, [1, 2, 3, 4, 5]), 1)

    def test_edge_case(self):
        self.assertEqual(frequency_Of_Largest(5, [5, 5, 5, 5, 5]), 5)

    def test_edge_case2(self):
        self.assertEqual(frequency_Of_Largest(5, [1, 1, 1, 1, 1]), 5)

    def test_edge_case3(self):
        self.assertEqual(frequency_Of_Largest(5, [2, 2, 2, 2, 2]), 1)

    def test_edge_case4(self):
        self.assertEqual(frequency_Of_Largest(5, [1, 2, 3, 4, 5]), 1)

    def test_edge_case5(self):
        self.assertEqual(frequency_Of_Largest(5, [5, 4, 3, 2, 1]), 1)

    def test_edge_case6(self):
        self.assertEqual(frequency_Of_Largest(5, [1, 1, 2, 2, 3]), 1)

    def test_edge_case7(self):
        self.assertEqual(frequency_Of_Largest(5, [1, 2, 3, 4, 5]), 1)

    def test_edge_case8(self):
        self.assertEqual(frequency_Of_Largest(5, [5, 5, 5, 5, 5]), 5)

    def test_edge_case9(self):
        self.assertEqual(frequency_Of_Largest(5, [1, 1, 1, 1, 1]), 5)

    def test_edge_case10(self):
        self.assertEqual(frequency_Of_Largest(5, [2, 2, 2, 2, 2]), 1)
