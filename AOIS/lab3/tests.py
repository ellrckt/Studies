import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from lab.main import Sdnf
class TestSdnf(unittest.TestCase):
    
    def test_simple_expression(self):
        sdnf = Sdnf("a")
        self.assertEqual(sdnf.minimaized_sdnf, [[]])
        self.assertEqual(sdnf.letters, ['a'])
        
    def test_expression_with_negation(self):
        sdnf = Sdnf("!a")
        self.assertEqual(sdnf.minimaized_sdnf, [[]])
        self.assertEqual(sdnf.letters, ['a'])
        
    def test_expression_with_multiple_variables(self):
        sdnf = Sdnf("(!abc)|(a!b!c)|(a!bc)|(ab!c)")
        self.assertEqual(sdnf.minimaized_sdnf, [['A', 'b', 'c'], ['a', 'B'], ['a', 'C']])
        self.assertEqual(sdnf.letters, ['a', 'b', 'c'])
        
    def test_expression_with_redundant_terms(self):
        sdnf = Sdnf("(a!b!c)|(a!bc)|(a!b!c)")
        self.assertEqual(sdnf.minimaized_sdnf, [['a', 'B']])
        self.assertEqual(sdnf.letters, ['a', 'b', 'c'])
        
    def test_calc_table_method(self):
        sdnf = Sdnf("(!abc)|(a!b!c)|(a!bc)|(ab!c)")
        sdnf.calc_table_method()
        self.assertEqual(sdnf.calc_method, ['A, b, c', 'a, B', 'a, C'])
        
    def test_format_strings(self):
        sdnf = Sdnf("!a&b&c")
        formatted = sdnf.format_strings("!a&b&c")
        self.assertEqual(formatted, [['b']])
        
    def test_find_inter(self):
        sdnf = Sdnf("(!a&b&c)|(a&!b&!c)")
        intersected = sdnf.find_inter([['A', 'b', 'c'], ['a', 'B', 'C']])
        self.assertEqual(intersected, [['A', 'b', 'c'], ['a', 'B', 'C']])

if __name__ == '__main__':
    unittest.main()
