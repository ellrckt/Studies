import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from lab.main import HashTable
import unittest
import unittest

class TestHashTable(unittest.TestCase):
    def setUp(self):
        self.hash_table = HashTable(11)
    
    def test_insert_and_search(self):
        self.hash_table.insert("apple", "Value1")
        self.hash_table.insert("banana", "Value2")
        self.hash_table.insert("grape", "Value3")
        
        self.assertEqual(self.hash_table.search("apple"), "Value1")
        self.assertEqual(self.hash_table.search("banana"), "Value2")
        self.assertEqual(self.hash_table.search("grape"), "Value3")
    
    def test_search_nonexistent_key(self):
        self.hash_table.insert("apple", "Value1")
        self.assertIsNone(self.hash_table.search("nonexistent"))
    
    def test_search(self):
        self.hash_table.insert('apple','Value1')
        a = self.hash_table.search('apple')
        self.assertEqual(a,'Value1')
        
    def test_delete(self):
        self.hash_table.insert("apple", "Value1")
        self.hash_table.insert("banana", "Value2")
        self.hash_table.delete("banana")
        
        self.assertIsNone(self.hash_table.search("banana"))
        self.assertEqual(self.hash_table.search("apple"), "Value1")
    
    def test_overwrite_value(self):
        self.hash_table.insert("apple", "Value1")
        self.hash_table.insert("apple", "Value2")
        
        self.assertEqual(self.hash_table.search("apple"), "Value2")
    
    def test_hash_table_full(self):
        with self.assertRaises(Exception) as context:
            for i in range(12):
                self.hash_table.insert(f"key{i}", f"Value{i}")
        
        self.assertTrue("Хеш-таблица переполнена" in str(context.exception))
    
    def test_str_representation(self):
        self.hash_table.insert("whynot", "Value1")
        self.hash_table.insert("no", "Value2")
        self.hash_table.insert("yes", "Value3")
        self.hash_table.insert("okay", "Value4")
        self.hash_table.insert("qwerty", "Value5")
        self.hash_table.insert("qwertt", "Value6")
        self.hash_table.insert("acbbgd", "Value7")
        self.hash_table.insert("abcde", "Value8")
        self.hash_table.insert("abcd", "Value9")
        self.hash_table.insert("ab", "Value10")
        self.hash_table.insert("abc", "Value11")
        
        expected_str = (
            "Index 0: Key = abcde, Value = Value8\n"
            "Index 1: Key = no, Value = Value2\n"
            "Index 2: Key = qwerty, Value = Value5\n"
            "Index 3: Key = okay, Value = Value4\n"
            "Index 4: Key = ab, Value = Value10\n"
            "Index 5: Key = abc, Value = Value11\n"
            "Index 6: Key = abcd, Value = Value9\n"
            "Index 7: Key = yes, Value = Value3\n"
            "Index 8: Key = qwertt, Value = Value6\n"
            "Index 9: Key = acbbgd, Value = Value7\n"
            "Index 10: Key = whynot, Value = Value1"
        )
        self.assertEqual(str(self.hash_table), expected_str)
    
    def test_delete_nonexistent_key(self):
        self.hash_table.insert("apple", "Value1")
        self.hash_table.delete("banana")
        self.assertEqual(self.hash_table.search("apple"), "Value1")
        self.assertIsNone(self.hash_table.search("banana"))
    
    def test_insert_many_items(self):
        items = [("apple", "Value1"), ("banana", "Value2"), ("grape", "Value3"), ("orange", "Value4"), ("lemon", "Value5"),
                ("lime", "Value6"), ("mango", "Value7"), ("peach", "Value8"), ("cherry", "Value9"), ("pear", "Value10"),
                ("plum", "Value11")]

        for key, value in items:
            self.hash_table.insert(key, value)

        for key, value in items:
            self.assertEqual(self.hash_table.search(key), value)

    def test_delete_and_reinsert(self):
        self.hash_table.insert("apple", "Value1")
        self.hash_table.delete("apple")
        self.assertIsNone(self.hash_table.search("apple"))
        self.hash_table.insert("apple", "Value2")
        self.assertEqual(self.hash_table.search("apple"), "Value2")

    def test_collision_handling(self):
        self.hash_table.insert("apple", "Value1")
        self.hash_table.insert("papel", "Value2")
        self.hash_table.insert("pleap", "Value3")

        self.assertEqual(self.hash_table.search("apple"), "Value1")
        self.assertEqual(self.hash_table.search("papel"), "Value2")
        self.assertEqual(self.hash_table.search("pleap"), "Value3")

#coverage run -m unittest discover

if __name__ == "__main__":
    unittest.main()
