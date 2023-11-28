import hashlib

class HashTable:
    class PairKeyValue:
        def __init__(self, key, value):
            self.key = key
            self.value = value

    def __init__(self):
        self.num_tables = 5
        self.table = [[] for _ in range(self.num_tables)]
        self.length = 0

        self.low_percentage = 0.25
        self.max_percentage = 0.75

        self.growth_table = self.reduce_table = 2

    def hash(self, key):
        encode = key.encode()
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

    def update(self, new_capacity):
        old_table = self.table
        self.length = 0
        self.num_tables = new_capacity
        self.table = [[] for _ in range(new_capacity)]
        for array in old_table:
            for pair in array:
                self.__setitem__(pair.key, pair.value)


table = HashTable()
