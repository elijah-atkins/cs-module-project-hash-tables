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

    def insert_at_head(self, node):
        node.next = self.head
        self.head = node
    
    def insert_at_head_or_overwrite(self, node):
        node.next = self.head
        self.head = node

    def find(self, value):
        #return node w/ value
        current = self.head
        # walk the linked list
        while current is not None:
            if current.value == value:
                # Found it!
                return current
            current = current.next
        return None

    #delete node w/ given value then return that node
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