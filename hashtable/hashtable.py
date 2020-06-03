class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8

class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys
    Implement this.
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.count = 0
        self.storage = [None] * capacity


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)
        One of the tests relies on this.
        Implement this.
        """
        return self.capacity


    def get_load_factor(self):
        """
        Return the load factor for this hash table.
        Implement this.
        """
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
        # Loop the key so we can hash every char
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
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.
        Hash collisions should be handled with Linked List Chaining.
        Implement this.
        """
        # Create a hash index
        index = self.hash_index(key)

        # Insert into an empty slot
        if not self.storage[index]:
            self.storage[index] = HashTableEntry(key, value)
            # Add to the items stored (count)
            self.count += 1

        # If linked list exists at current location
        else:
            current_node = self.storage[index]

            while current_node.key != key and current_node.next:
                current_node = current_node.next

            # If key found, update current value
            if current_node.key == key:
                current_node.value = value

            # Cannot find the key, end of list. Create a new entry.
            else:
                current_node.next = HashTableEntry(key, value)
                self.count += 1

        # Resize hash table if load factor too large
        if self.get_load_factor() > 0.7:
            # over loaded load Factor > 0.7
            self.resize(self.capacity * 2)


    def delete(self, key):
        """
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        Implement this.
        """
        index = self.hash_index(key)
        current_node = self.storage[index]

        # if nothing in the index
        if not current_node:
            print('Nothing to see here...')

        # If value to delete is at the head of the list
        elif not current_node.next:
            self.storage[index] = None
            self.count -= 1

        else:
            # store a pointer to previous node
            previous_node = None

            # Move to the next node if key won't match and there is next node
            while current_node.key != key and current_node.next:
                previous_node = current_node
                current_node = current_node.next

            # Value to delete is in the middle, reassign around this node
            if not current_node.next:
                previous_node.next = None
                self.items_stored -= 1
            else:
                previous_node.next = current_node.next
                self.count -= 1

        # Resize hash table if load factor is too small
        if self.get_load_factor() < 0.2:
            # underloaded Load Factor < 0.2
            self.resize(min(self.capacity // 2, MIN_CAPACITY))



    def get(self, key):
        """
        Retrieve the value stored with the given key.
        Returns None if the key is not found.
        Implement this.
        """
        index = self.hash_index(key)

        if self.storage[index]:
            current_node = self.storage[index]

            # If key does not match move to the next node if there is any
            while current_node.key != key and current_node.next:
                current_node = current_node.next
                
            # Cannot find the key
            if not current_node.next:
                return current_node.value

            # Otherwise: found the correct node
            else:
                return current_node.value

        # No LL here, return none
        else:
            return None

  
    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.
        Implement this.
        """
        # Store existing array values
        existing_storage = self.storage

        # Start a new hash table and update
        self.capacity = new_capacity
        self.storage = [None] * new_capacity

        # Add to the new table
        for item in existing_storage:
            # If item is a LL, add all nodes to new storage
            if item:
                current_node = item
                while current_node:
                    # put current key/value into new storage
                    self.put(current_node.key, current_node.value)
                    current_node = current_node.next


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
