import unittest
from mbpp_449_code import check_Triangle

class TestCheckTriangle(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(check_Triangle(0,0,1,1,2,2), 'Yes')

    def test_edge_case(self):
        self.assertEqual(check_Triangle(0,0,0,0,0,0), 'No')

    def test_edge_case2(self):
        self.assertEqual(check_Triangle(0,0,1,1,1,1), 'Yes')

    def test_edge_case3(self):
        self.assertEqual(check_Triangle(0,0,1,1,2,2), 'Yes')

    def test_edge_case4(self):
        self.assertEqual(check_Triangle(0,0,0,0,1,1), 'No')

    def test_edge_case5(self):
        self.assertEqual(check_Triangle(0,0,0,0,0,0), 'No')

    def test_edge_case6(self):
        self.assertEqual(check_Triangle(0,0,1,1,0,0), 'No')

    def test_edge_case7(self):
        self.assertEqual(check_Triangle(0,0,0,0,1,1), 'No')

    def test_edge_case8(self):
        self.assertEqual(check_Triangle(0,0,1,1,1,1), 'Yes')

    def test_edge_case9(self):
        self.assertEqual(check_Triangle(0,0,0,0,0,0), 'No')

    def test_edge_case10(self):
        self.assertEqual(check_Triangle(0,0,1,1,2,2), 'Yes')
