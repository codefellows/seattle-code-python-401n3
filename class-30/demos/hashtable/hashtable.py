    """
    Start of Hashtable implementation.
    Use as a basis for your own work.
    No guarantees that it's perfect.
    Making it perfect is your job.
    """

# NOTE: Use your own LinkedList implementations instead
from codefellows.dsa.linked_list import LinkedList


class Hashtable:
    def __init__(self, size=1024):
        self.size = size
        self.buckets = [None] * self.size

    def hash(self, key):
        sum = 0
        for char in key:
            numeric_value = ord(char)
            sum += numeric_value

        product = sum * 599

        index = product % self.size

        return index

    def add(self, key, value):

        index = self.hash(key)

        if not self.buckets[index]:
            self.buckets[index] = LinkedList()

        bucket = self.buckets[index]

        bucket.insert([key, value])
