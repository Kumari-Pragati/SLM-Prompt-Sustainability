import unittest
from mbpp_186_code import check_literals

class TestCheckLiterals(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(check_literals('Hello, World!', ['World']), 'Matched!')

    def test_edge_case(self):
        self.assertEqual(check_literals('Hello, World!', ['Python']), 'Not Matched!')

    def test_boundary_case(self):
        self.assertEqual(check_literals('', ['']), 'Not Matched!')

    def test_corner_case(self):
        self.assertEqual(check_literals('Hello, World!', []), 'Not Matched!')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            check_literals(123, ['World'])
