class HashTable:
    def __init__(self, size=11):
        self.size = size
        self.table = [None] * size

    def string_to_int(self, key):
        return sum(ord(char) for char in key)

    def primary_hash(self, key):
        key_int = self.string_to_int(key)
        return key_int % self.size

    def secondary_hash(self, key):
        key_int = self.string_to_int(key)
        return 1 + (key_int % (self.size - 1))

    def double_hash(self, key, i):
        return (self.primary_hash(key) + i * self.secondary_hash(key)) % self.size

    def insert(self, key, value):
        for i in range(self.size):
            idx = self.double_hash(key, i)
            if self.table[idx] is None or self.table[idx][0] == key:
                self.table[idx] = (key, value)
                return
        raise Exception("Хеш-таблица переполнена")

    def search(self, key):
        for i in range(self.size):
            idx = self.double_hash(key, i)
            if self.table[idx] is None:
                return None
            if self.table[idx][0] == key:
                return self.table[idx][1]
        return None

    def delete(self, key):
        for i in range(self.size):
            idx = self.double_hash(key, i)
            if self.table[idx] is None:
                return
            if self.table[idx][0] == key:
                self.table[idx] = None
                return

    def __str__(self):
        result = []
        for i, entry in enumerate(self.table):
            if entry is not None:
                result.append(f"Index {i}: Key = {entry[0]}, Value = {entry[1]}")
            else:
                result.append(f"Index {i}: Empty")
        return "\n".join(result)


if __name__ == "__main__":
    hash_table = HashTable(11)

#     hash_table.insert("whynot", "Value1")
#     hash_table.insert("no", "Value2")
#     hash_table.insert("yes", "Value3")
#     hash_table.insert("okay", "Value4")
#     hash_table.insert("qwerty", "Value5")
#     hash_table.insert("qwertt", "Value6")
#     hash_table.insert("acbbgd", "Value7")
#     hash_table.insert("abcde", "Value8")
#     hash_table.insert("abcd", "Value9")
#     hash_table.insert("ab", "Value10")
#     hash_table.insert("abc", "Value11")
#     print(hash_table.search('abc'))
#     print("Хеш-таблица после вставки:")
#     print(hash_table)
#     print("Поиск ключа 'abc':", hash_table.search("abc"))
#     hash_table.delete("abc")
#     print("\nХеш-таблица после удаления ключа 'abc':")
#     print(hash_table)
# print(hash_table)
