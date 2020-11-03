from linked_list import LinkedList
from linked_list import Node


class HashTableEntry:
    """
    Linked List hash table key/value pair
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __eq__(self, other):
        if isinstance(other, HashTableEntry):
            return self.key == other.key
        return False


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys
    Implement this.
    """

    def __init__(self, capacity = MIN_CAPACITY):
        # Your code here
        self.capacity = capacity
        self.table = [None] * capacity
        self.num_elements = 0

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
        if self.num_elements != 0:
            return  self.num_elements /self.capacity 
        else:
            return 0

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit
        Implement this, and/or DJB2.
        """

        seed = 0
        # 64 bit FNV_prime = 240 + 28 + 0xb3 = 1099511628211
        FNV_prime = 1099511628211
        # 64 bit offset basis
        offset_basis = 14695981039346656037

        # FNV hash algorithm
        hash = offset_basis + seed
        for char in key:
            hash = hash * FNV_prime
            hash = hash ^ ord(char)
        return hash

    def djb2(self, key):
        """
        DJB2 hash, 32-bit
        Implement this, and/or FNV-1.
        """
        # djb2 hash
        hash = 5381
        for char in key:
            hash = ((hash << 5) + hash) + ord(char)
        return hash & 0xffffffff

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.
        Hash collisions should be handled with Linked List Chaining.
        Implement this.
        """

        hash_index = self.hash_index(key)
        if self.table[hash_index] != None:
            linked_list = self.table[hash_index]
            did_add_new_node = linked_list.insert_at_head_or_overwrite(
                Node(HashTableEntry(key, value)))
            if did_add_new_node:
                self.num_elements += 1
        else:
            linked_list = LinkedList()
            linked_list.insert_at_head(Node(HashTableEntry(key, value)))
            self.table[hash_index] = linked_list
            self.num_elements += 1
        if self.get_load_factor() > 0.7:
            self.resize(self.get_num_slots() * 2)

    def delete(self, key):
        """
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        Implement this.
        """
        hash_index = self.hash_index(key)
        if self.table[hash_index] != None:
            linked_list = self.table[hash_index]
            did_delete_node = linked_list.delete(HashTableEntry(key, None))
            if did_delete_node != None:
                self.num_elements -= 1

                if self.get_load_factor() < 0.2:
                    if self.capacity > 8:
                        self.resize(int(self.get_num_slots() / 2))

        else:
            print("Warning: node not found")


    def get(self, key):
        hash_index = self.hash_index(key)
        if self.table[hash_index] != None:
            linked_list = self.table[hash_index]
            node = linked_list.find(HashTableEntry(key, None))
            if node != None:
                return node.value.value
        return None

    def resize(self, new_capacity):
        """
            Changes the capacity of the hash table and
            rehashes all key/value pairs.
            Implement this.
            """
        old_table = self.table
        self.table = [None] * int(new_capacity)
        self.capacity = new_capacity 
        self.num_elements = 0

        for element in old_table:
            if element == None:
                continue
            curr_node = element.head
            while curr_node != None:
                temp = curr_node.get_next()
                curr_node.next = None
                hash_index = self.hash_index(curr_node.value.key)

                if self.table[hash_index] != None:
                    self.table[hash_index].insert_at_head(curr_node)
                else:
                    linked_list = LinkedList()
                    linked_list.insert_at_head(curr_node)
                    self.table[hash_index] = linked_list
                curr_node = temp
                self.num_elements += 1



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
