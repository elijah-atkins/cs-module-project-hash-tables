class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return f'Node({repr(self.value)})'

class LinkedList:
    def __init__(self):
        self.head = None
    def __repr__(self):
        result = ""
        current = self.head
        while current is not None:
            result += f'({current.value})'
            if current.next is not None:
                result += ' -> '
            current = current.next
        return result
    def current_value(self, node):
        return node.head.value
    #insert node at head of list
    #runtime: O(1)
    def insert_at_head(self, node):
        node.next = self.head
        self.head = node
    
    # overwrite node or insert node at head
    # runtime: O(n)
    def insert_at_head_or_overwrite(self, node):
        existingNode = self.find(node.value) # O(n)
        if existingNode != None:
            existingNode.value = node.value
        else:
            self.insert_at_head(node) # O(1)
    
    #return node w/ value
    # runtime O(n) where n = number of nodes
    def find(self, value):
        current = self.head
        # walk the linked list
        while current is not None:
            if current.value == value:
                # Found it!
                return current
            current = current.next
        return None

    #delete node w/ given value then return that node
    #runtime: O(n) where n = number of nodes
    def delete(self, value):
        current = self.head

        # Special case of deleting the head of the list
        if current.value == value:
            self.head = current.next
            current.next = None
            return current

        # two pointers
        previous = current
        current = current.next

        while current is not None:
            if current.value == value:  # Delete this one
                previous.next = current.next   # Cuts out the old node
                current.next = None 
                return current
            else:
                previous = previous.next
                current = current.next
        return None 

# a = Node(1)
# b = Node(2)
# c = Node(3)
# ll = LinkedList()
# ll.insert_at_head(c)
# ll.insert_at_head(b)
# ll.insert_at_head(a)
# ll.insert_at_head_or_overwrite(c)
# ll.delete(3)
# print(ll)