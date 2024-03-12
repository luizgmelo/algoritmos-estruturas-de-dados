import hashlib

# importing LinkedList
import sys
sys.path.append("../LinkedList/")
from Linked_list import LinkedList

class HashTable:
    class PairKeyValue:
        def __init__(self, key, value):
            self.key = key
            self.value = value

    def __init__(self):
        self.num_tables = 5
        self.table = [LinkedList() for _ in range(self.num_tables)]
        self.length = 0

        self.low_percentage = 0.25
        self.max_percentage = 0.75

        self.growth_table = self.reduce_table = 2

    def hash(self, key):
        encode = str(key).encode()
        return int(hashlib.sha256(encode).hexdigest(), 16) % self.num_tables

    @property
    def capacity_percentage_used(self):
        return self.length // self.num_tables

    def __setitem__(self, key, value):
        if self.capacity_percentage_used > self.max_percentage:
            new_capacity = self.num_tables * 2
            self.update(new_capacity)
        
        index = self.hash(key)
        for pair in self.table[index]:
            if pair.key == key:
                pair.value = value
                return

        self.table[index].append(self.PairKeyValue(key, value))
        self.length += 1
    
    def __getitem__(self, key):
        index = self.hash(key)
        for pair in self.table[index]:
            if pair.key == key:
                return pair.value
        raise KeyError('Invalid key')

    def __delitem__(self, key):
        if self.capacity_percentage_used < self.low_percentage:
            new_capacity = self.num_tables // 2
            self.update(new_capacity)

        index = self.hash(key)
        for pair in self.table[index]:
            if pair.key == key:
                self.table[index].remove(pair)
                self.length -= 1
                return
        raise KeyError('Invalid key')

    def update(self, new_capacity):
        old_table = self.table
        self.length = 0
        self.num_tables = new_capacity
        self.table = [LinkedList() for _ in range(new_capacity)]
        for array in old_table:
            for pair in array:
                self.__setitem__(pair.key, pair.value)

if __name__ == "__main__":
    table = HashTable()
    table["0000-0000"] = "Guilherme"
    table["0000-0001"] = "Rafael"
    table["0000-0002"] = "Richard"
    table["0000-0003"] = "Leandro"
    table["0000-0004"] = "Wagner"
    table["0000-0005"] = "Abreu"
    del table["0000-0000"]
    del table["0000-0001"]
    del table["0000-0002"]

    # print(table["0000-0000"])
    # print(table["0000-0001"])
    # print(table["0000-0002"])
    print(table["0000-0003"])
    print(table["0000-0004"])
    print(table["0000-0005"])
