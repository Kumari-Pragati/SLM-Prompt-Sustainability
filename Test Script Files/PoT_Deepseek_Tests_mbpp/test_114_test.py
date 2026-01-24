import unittest
from mbpp_114_code import assign_freq

class TestAssignFreq(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(assign_freq([1, 2, 2, 3, 3, 3]), "[(1, 1), (2, 2), (3, 3)]")

    def test_empty_list(self):
        self.assertEqual(assign_freq([]), "[]")

    def test_single_element(self):
        self.assertEqual(assign_freq([1]), "[(1, 1)]")

    def test_duplicate_elements(self):
        self.assertEqual(assign_freq([1, 1, 1]), "[(1, 3)]")

    def test_large_number_of_elements(self):
        self.assertEqual(assign_freq(list(range(1, 101))), list(map(lambda x: (x, 1), range(1, 101))))

    def test_negative_numbers(self):
        self.assertEqual(assign_freq([-1, -1, 1]), "[(-1, 2), (1, 1)]")

    def test_mixed_numbers(self):
        self.assertEqual(assign_freq([1, -1, 1, -1]), "[(-1, 2), (1, 2)]")
