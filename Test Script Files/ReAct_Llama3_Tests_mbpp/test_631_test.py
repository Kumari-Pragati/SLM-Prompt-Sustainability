import unittest
from mbpp_631_code import replace_spaces

class TestReplaceSpaces(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(replace_spaces('Python Exercises'), 'Python_Exercises')

    def test_edge_case_empty_string(self):
        self.assertEqual(replace_spaces(''), '')

    def test_edge_case_single_space(self):
        self.assertEqual(replace_spaces('a'), 'a')

    def test_edge_case_multiple_spaces(self):
        self.assertEqual(replace_spaces('a b c'), 'a_b_c')

    def test_edge_case_multiple_spaces_with_newline(self):
        self.assertEqual(replace_spaces('a b\nc'), 'a_b_c')

    def test_edge_case_multiple_spaces_with_tabs(self):
        self.assertEqual(replace_spaces('a\tb\nc'), 'a_b_c')

    def test_edge_case_multiple_spaces_with_newline_and_tabs(self):
        self.assertEqual(replace_spaces('a\tb\nc\n'), 'a_b_c')

    def test_edge_case_spaces_and_non_spaces(self):
        self.assertEqual(replace_spaces('a b c d e f g h i j k l m n o p q r s t u v w x y z'), 'a_b_c_d_e_f_g_h_i_j_k_l_m_n_o_p_q_r_s_t_u_v_w_x_y_z')
