import unittest
from HashTable import HashTable

class TestHashTableMethods(unittest.TestCase):
    def test_hash(self):
        """
        Test that hash are numbers between 0 and 4 num_tables
        """
        my_hash_table = HashTable()
        x = my_hash_table.hash("Guilherme")
        y = my_hash_table.hash(12)
        z = my_hash_table.hash(True)
        n = my_hash_table.hash([])
        self.assertTrue(0 <= x < 5)
        self.assertTrue(0 <= y < 5)
        self.assertTrue(0 <= z < 5)
        self.assertTrue(0 <= n < 5)

    def test_setitem(self):
        """
        Test that can set item on hash table
        """
        my_hash_table = HashTable()
        my_hash_table["luiz"] = 40028922
        # hash is four
        # print(my_hash_table.hash("luiz"))
        my_hash_table[42] = "the answer to life the universe and everything"
        # hash is three
        # print(my_hash_table.hash(42))
        my_hash_table[True] = True
        # hash is zero
        # print(my_hash_table.hash(True))
        my_hash_table[[]] = "lol"
        # hash is three
        # print(my_hash_table.hash([]))

        
        # Check keys are there
        self.assertEqual(my_hash_table.table[4].head.data.key, "luiz")
        self.assertEqual(my_hash_table.table[3].head.data.key, 42)
        self.assertEqual(my_hash_table.table[0].head.data.key, True)
        self.assertEqual(my_hash_table.table[3].head.next.data.key, [])

        # Check values are there
        self.assertEqual(my_hash_table.table[4].head.data.value, 40028922)
        self.assertEqual(my_hash_table.table[3].head.data.value, "the answer to life the universe and everything")
        self.assertEqual(my_hash_table.table[0].head.data.value, True)
        self.assertEqual(my_hash_table.table[3].head.next.data.value, "lol")

    def test_getitem(self):
        """
        Test that can get item on hash table
        """
        my_hash_table = HashTable()
        my_hash_table["luiz"] = "gmelo"
        my_hash_table[42] = "the answer to life the universe and everything"
        my_hash_table[111] = 222
        my_hash_table[True] = True
        my_hash_table[[]] = "lol"

        self.assertEqual(my_hash_table["luiz"], "gmelo")
        self.assertEqual(my_hash_table[42], "the answer to life the universe and everything")
        self.assertEqual(my_hash_table[111], 222)
        self.assertEqual(my_hash_table[True], True)
        self.assertEqual(my_hash_table[[]], "lol")

        with self.assertRaises(KeyError):
            my_hash_table["minecraft"]
            my_hash_table[999]
            my_hash_table[False]

    def test_delitem(self):
        """
        Test that can delete an item on hash table
        """
        my_hash_table = HashTable()
        my_hash_table["luiz"] = "gmelo"
        my_hash_table[42] = "the answer to life the universe and everything"
        my_hash_table[111] = 222
        my_hash_table[True] = True
        my_hash_table[[]] = "lol"

        del my_hash_table["luiz"]
        del my_hash_table[42]
        del my_hash_table[111]
        del my_hash_table[True]
        del my_hash_table[[]]

        with self.assertRaises(KeyError):
            my_hash_table["luiz"]
            my_hash_table[42]
            my_hash_table[111]
            my_hash_table[True]
            my_hash_table[[]]
    

    def test_update(self):
        """
        Test that table increase when is use 75% more use and decrease 25%
        """
        my_hash_table = HashTable()
        self.assertEqual(my_hash_table.num_tables, 5)
        my_hash_table["0000-0000"] = "Guilherme"
        my_hash_table["0000-0001"] = "Rafael"
        my_hash_table["0000-0002"] = "Richard"
        my_hash_table["0000-0003"] = "Leandro"
        my_hash_table["0000-0004"] = "Wagner"
        # 100% used
        self.assertEqual(my_hash_table.num_tables, 10)
        

        del my_hash_table["0000-0000"]
        del my_hash_table["0000-0001"]
        del my_hash_table["0000-0002"]
        del my_hash_table["0000-0003"]
        # 20% used
        self.assertEqual(my_hash_table.num_tables, 5)
        del my_hash_table["0000-0004"]
        # 0% used
        self.assertEqual(my_hash_table.num_tables, 2)


if __name__ == "__main__":
    unittest.main()
