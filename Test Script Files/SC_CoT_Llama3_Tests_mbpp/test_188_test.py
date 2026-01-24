import unittest
from mbpp_188_code import prod_Square

class TestProdSquare(unittest.TestCase):

    def test_true_output(self):
        self.assertTrue(prod_Square(36))

    def test_false_output(self):
        self.assertFalse(prod_Square(10))

    def test_edge_case(self):
        self.assertTrue(prod_Square(25))

    def test_edge_case_false(self):
        self.assertFalse(prod_Square(24))

    def test_edge_case_true(self):
        self.assertTrue(prod_Square(49))

    def test_edge_case_false2(self):
        self.assertFalse(prod_Square(50))

    def test_edge_case_true2(self):
        self.assertTrue(prod_Square(64))

    def test_edge_case_false3(self):
        self.assertFalse(prod_Square(65))

    def test_edge_case_true3(self):
        self.assertTrue(prod_Square(81))

    def test_edge_case_false4(self):
        self.assertFalse(prod_Square(82))

    def test_edge_case_true4(self):
        self.assertTrue(prod_Square(100))

    def test_edge_case_false5(self):
        self.assertFalse(prod_Square(101))

    def test_edge_case_true5(self):
        self.assertTrue(prod_Square(121))

    def test_edge_case_false6(self):
        self.assertFalse(prod_Square(122))

    def test_edge_case_true6(self):
        self.assertTrue(prod_Square(144))

    def test_edge_case_false7(self):
        self.assertFalse(prod_Square(145))

    def test_edge_case_true7(self):
        self.assertTrue(prod_Square(169))

    def test_edge_case_false8(self):
        self.assertFalse(prod_Square(170))

    def test_edge_case_true8(self):
        self.assertTrue(prod_Square(196))

    def test_edge_case_false9(self):
        self.assertFalse(prod_Square(197))

    def test_edge_case_true9(self):
        self.assertTrue(prod_Square(225))

    def test_edge_case_false10(self):
        self.assertFalse(prod_Square(226))

    def test_edge_case_true10(self):
        self.assertTrue(prod_Square(256))

    def test_edge_case_false11(self):
        self.assertFalse(prod_Square(257))

    def test_edge_case_true11(self):
        self.assertTrue(prod_Square(289))

    def test_edge_case_false12(self):
        self.assertFalse(prod_Square(290))

    def test_edge_case_true12(self):
        self.assertTrue(prod_Square(324))

    def test_edge_case_false13(self):
        self.assertFalse(prod_Square(325))

    def test_edge_case_true13(self):
        self.assertTrue(prod_Square(361))

    def test_edge_case_false14(self):
        self.assertFalse(prod_Square(362))

    def test_edge_case_true14(self):
        self.assertTrue(prod_Square(400))

    def test_edge_case_false15(self):
        self.assertFalse(prod_Square(401))

    def test_edge_case_true15(self):
        self.assertTrue(prod_Square(441))

    def test_edge_case_false16(self):
        self.assertFalse(prod_Square(442))

    def test_edge_case_true16(self):
        self.assertTrue(prod_Square(484))

    def test_edge_case_false17(self):
        self.assertFalse(prod_Square(485))

    def test_edge_case_true17(self):
        self.assertTrue(prod_Square(529))

    def test_edge_case_false18(self):
        self.assertFalse(prod_Square(530))

    def test_edge_case_true18(self):
        self.assertTrue(prod_Square(576))

    def test_edge_case_false19(self):
        self.assertFalse(prod_Square(577))

    def test_edge_case_true19(self):
        self.assertTrue(prod_Square(625))

    def test_edge_case_false20(self):
        self.assertFalse(prod_Square(626))
