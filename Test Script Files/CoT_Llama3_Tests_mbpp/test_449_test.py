import unittest
from mbpp_449_code import check_Triangle

class TestCheckTriangle(unittest.TestCase):
    def test_valid_triangle(self):
        self.assertEqual(check_Triangle(0,0,1,1,2,2), 'Yes')

    def test_non_valid_triangle(self):
        self.assertEqual(check_Triangle(0,0,1,1,0,0), 'No')

    def test_edge_case(self):
        self.assertEqual(check_Triangle(0,0,0,0,1,1), 'Yes')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            check_Triangle('a',1,2,3,4,5)

    def test_invalid_input2(self):
        with self.assertRaises(TypeError):
            check_Triangle(0,'a',2,3,4,5)

    def test_invalid_input3(self):
        with self.assertRaises(TypeError):
            check_Triangle(0,1,'a',2,3,4)

    def test_invalid_input4(self):
        with self.assertRaises(TypeError):
            check_Triangle(0,1,2,'a',3,4)

    def test_invalid_input5(self):
        with self.assertRaises(TypeError):
            check_Triangle(0,1,2,3,'a',4)

    def test_invalid_input6(self):
        with self.assertRaises(TypeError):
            check_Triangle(0,1,2,3,4,'a')
