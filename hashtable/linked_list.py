class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return f'Node({repr(self.value)})'

class LinkedList:
    def __init__(self):
        self.head = None
    def __str__(self):
        result = ""
        current = self.head

        while current is not None:
            result += f'({current.value})'
            if current.next is not None:
                result += ' -> '
            current = current.next
        return r

    def insert_at_head(self, node):
        node.next = self.head
        self.head = node

    def find(self, value):
        current = self.head
        # walk the linked list
        while current is not None:
            if current.value == value:
                # Found it!
                return current
            current = current.next
        return None

    def delete(self, value):
        current = self.head

        # Special case of deleting the head of the list
        if current.value == value:
            self.head = self.head.next
            return current

        # General case
        prev = current
        current = current.next

        while current is not None:
            if current.value == value:  # Delete this one
                prev.next = current.next   # Cuts out the old node
                return current
            else:
                prev = prev.next
                current = current.next
        return None 