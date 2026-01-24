import unittest
from mbpp_639_code import sample_nam

class TestSampleNam(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(sample_nam(['Apple', 'Banana', 'Cherry']), 10)

    def test_edge_case_empty_list(self):
        self.assertEqual(sample_nam([]), 0)

    def test_boundary_case_single_element(self):
        self.assertEqual(sample_nam(['apple']), 0)
        self.assertEqual(sample_nam(['Apple']), 5)

    def test_corner_case_all_capital(self):
        self.assertEqual(sample_nam(['APPLE', 'BANANA', 'CHERRY']), 0)

    def test_corner_case_all_lower(self):
        self.assertEqual(sample_nam(['apple', 'banana', 'cherry']), 0)

    def test_corner_case_mixed_case(self):
        self.assertEqual(sample_nam(['ApPle', 'BaNaNa', 'ChErRy']), 5)
