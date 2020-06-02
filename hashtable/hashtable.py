class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    # def __str__(self):
        

# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8

# A hash table is a data structure that can be searched through in O(1) time.

class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """
    def __init__(self, capacity):
        # Your code here
        self.capacity = capacity
        self.storage = [None] * capacity

        # Attributes for auto resize functionality
        self.count = 0
        self.resized = False
        self.is_resizing = False


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return self.capacity
        
# over loaded load Factor > 0.7
# underloaded Load Factor < 0.2
# resize the hash table
    def get_load_factor(self):
        """
        Return the load factor for this hash table.
        Implement this.
        """
        # nodes (count) / slots
        return self.count / self.capacity


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit
        Implement this, and/or DJB2.
        """
        # Your code here


    def djb2(self, key):
        """
        DJB2 hash, 32-bit
        Implement this, and/or FNV-1.
        """
        # Your code here
        hash = 5381
        for c in key:
            # The ord() function returns an integer representing the Unicode character.
            hash = (hash * 33) + ord(c)
        return hash


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        # Get the index where to store key/value. 
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.
        Hash collisions should be handled with Linked List Chaining.
        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        self.count += 1
        if not self.storage[index]:
            self.storage[index] = HashTableEntry(key, value)
            self.auto_resize()
        else:
            current_node = self.storage[index]
            while current_node:
                if current_node.key == key:
                    current_node.value = value
                    self.auto_resize()
                    return

                previous_node = current_node
                current_node = current_node.next

            previous_node.next = HashTableEntry(key, value)
            self.auto_resize()


    def delete(self, key):
        """
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        Implement this.
        """
        index = self.hash_index(key)
        value = self.storage[index].value
        self.storage[index].value = None

        # if self.get_load_factor() < 0.2:
        #     self.resize(min(self.capacity) // 2, MIN_CAPACITY)
        return value


    def get(self, key):
        """
        Retrieve the value stored with the given key.
        Returns None if the key is not found.
        Implement this.
        """
        index = self.hash_index(key)
        return self.storage[index].value


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.
        Implement this.
        """
        self.is_resizing = True
        self.capacity = new_capacity
        prev_storage = self.storage
        self.storage = [None] * self.capacity
        self.count = 0
        for index in range(len(prev_storage)):
            current_node = prev_storage[index]
            while current_node:
                self.put(current_node.key, current_node.value)
                current_node = current_node.next

            self.is_resizing = False
            self.resized = True
        
    def resize_check(self):
        load_factor = self.get_load_factor()
        if self.resized:
            if load_factor > 0.7:
                self.resize(2)
            elif load_factor < 0.2:
                self.resize(0.5)

    def auto_resize(self):
        if not self.is_resizing:
            self.resize_check()

# Linked list search: O(n)
# Linked list insert: O(1)
# BST search: O(log n)
# BST insert: O(log n)

if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
