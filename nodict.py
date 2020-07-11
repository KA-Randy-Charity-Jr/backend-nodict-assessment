#!/usr/bin/env python3
"""
Implementation of the NoDict assignment
"""

__author__ = '???'


class Node:
    def __init__(self, key, value=None):
        """set up the instances for the class object"""
        self.hash = hash(key)
        self.key = key
        self.value = value

    def __repr__(self):
        """print a human-readable representation
        of its key/value contents when asked"""
        return f'{self.__class__.__name__}({self.key}, {self.value})'

    def __eq__(self, other):
        """object to compare one key value with another"""
        return self.key == other.key

    def __hash__(self):
        """provide an instance for the hash value of the object"""
        return self.hash


class NoDict:
    def __init__(self, num_buckets=10):
        """class initializer to create the
        buckets according to a size parameter"""
        self.buckets = []
        for i in range(num_buckets):
            self.buckets.append([])
        self.num_buckets = num_buckets
        # Your code here

    def __repr__(self):
        """return a string representating the nodict contents"""

        return '\n'.join([f'{self.__class__.__name__}.{i}:{bucket}'
                          for i, bucket in enumerate(self.buckets)])

    def add(self, key, value):
        """"This class method should accept a new key and value,
        and store it into the `NoDict` instance."""
        # Your code here
        new_node = Node(key, value)
        index = hash(new_node) % self.num_buckets
        if new_node in self.buckets[index]:
            instance = self.buckets[index].index(new_node)
            self.buckets[index][instance] = new_node
        else:
            self.buckets[index].append(new_node)

        #     self.buckets[index].append(new_node)
        # else:
        #     self.buckets[index] = new_node

    def get(self, key):
        """" perform a key-lookup in the `NoDict` class"""
        new_key = Node(key)
        index = hash(new_key) % self.num_buckets
        if new_key not in self.buckets[index]:
            raise KeyError(f'{key} not found')
        return self.buckets[index][0].value

    def __getitem__(self, key):
        """retrieves the value of the key"""
        return self.get(key)

    def __setitem__(self, key, value):
        """sets an item in bucket"""
        self.add(key, value)
