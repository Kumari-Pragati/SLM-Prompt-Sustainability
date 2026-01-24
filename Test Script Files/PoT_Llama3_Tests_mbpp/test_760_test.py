import unittest
from mbpp_760_code import unique_Element

class TestUniqueElement(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(unique_Element([1,1,1,1],4), 'NO')

    def test_edge_case(self):
        self.assertEqual(unique_Element([1],1), 'YES')

    def test_edge_case2(self):
        self.assertEqual(unique_Element([1,2,3,4],4), 'NO')

    def test_edge_case3(self):
        self.assertEqual(unique_Element([1,1,2,2],4), 'NO')

    def test_edge_case4(self):
        self.assertEqual(unique_Element([1,1,1,2],4), 'NO')

    def test_edge_case5(self):
        self.assertEqual(unique_Element([1,1,1,1,2],5), 'NO')

    def test_edge_case6(self):
        self.assertEqual(unique_Element([1,1,1,1,1],5), 'YES')

    def test_edge_case7(self):
        self.assertEqual(unique_Element([],0), 'YES')

    def test_edge_case8(self):
        self.assertEqual(unique_Element([1],1), 'YES')

    def test_edge_case9(self):
        self.assertEqual(unique_Element([1,2],2), 'NO')

    def test_edge_case10(self):
        self.assertEqual(unique_Element([1,2,3,4,5],5), 'NO')
