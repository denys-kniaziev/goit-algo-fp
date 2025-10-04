class ListNode:
    """Node class for singly linked list"""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)


class LinkedList:
    """Singly linked list implementation"""
    def __init__(self):
        self.head = None

    def append(self, val):
        """Add element to the end of the list"""
        if not self.head:
            self.head = ListNode(val)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = ListNode(val)

    def to_list(self):
        """Convert linked list to Python list for display"""
        result = []
        current = self.head
        while current:
            result.append(current.val)
            current = current.next
        return result

    def from_list(self, values):
        """Create linked list from Python list"""
        self.head = None
        for val in values:
            self.append(val)


def reverse_linked_list(head):
    """
    Reverse a singly linked list by changing node connections
    Time complexity: O(n), Space complexity: O(1)
    """
    prev = None
    current = head
    
    while current:
        next_temp = current.next  # Store next node
        current.next = prev       # Reverse the link
        prev = current           # Move prev forward
        current = next_temp      # Move current forward
    
    return prev  # prev is now the new head


def insertion_sort_linked_list(head):
    """
    Sort linked list using insertion sort algorithm
    Time complexity: O(n²), Space complexity: O(1)
    """
    if not head or not head.next:
        return head
    
    # Create dummy node to simplify insertion
    dummy = ListNode(0)
    dummy.next = head
    prev = head
    current = head.next
    
    while current:
        if current.val >= prev.val:
            # Already in correct position
            prev = current
            current = current.next
        else:
            # Find correct position to insert current
            prev.next = current.next
            
            # Find insertion point
            insert_prev = dummy
            while insert_prev.next and insert_prev.next.val < current.val:
                insert_prev = insert_prev.next
            
            # Insert current node
            current.next = insert_prev.next
            insert_prev.next = current
            
            # Move to next node
            current = prev.next
    
    return dummy.next


def merge_sorted_lists(list1, list2):
    """
    Merge two sorted linked lists into one sorted list
    Time complexity: O(m+n), Space complexity: O(1)
    """
    dummy = ListNode(0)
    current = dummy
    
    while list1 and list2:
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
    
    # Append remaining nodes
    current.next = list1 or list2
    
    return dummy.next


def demo():
    """Demonstration of linked list operations"""
    print("=== Task 1: Linked List Operations ===")
    
    # Test reverse function
    print("\n1. Testing reverse function:")
    ll1 = LinkedList()
    ll1.from_list([1, 2, 3, 4, 5])
    print(f"Original: {ll1.to_list()}")
    ll1.head = reverse_linked_list(ll1.head)
    print(f"Reversed: {ll1.to_list()}")
    
    # Test sorting function
    print("\n2. Testing insertion sort:")
    ll2 = LinkedList()
    ll2.from_list([64, 34, 25, 12, 22, 11, 90])
    print(f"Original: {ll2.to_list()}")
    ll2.head = insertion_sort_linked_list(ll2.head)
    print(f"Sorted: {ll2.to_list()}")
    
    # Test merge function
    print("\n3. Testing merge of two sorted lists:")
    ll3 = LinkedList()
    ll3.from_list([1, 3, 5, 7])
    ll4 = LinkedList()
    ll4.from_list([2, 4, 6, 8])
    print(f"List 1: {ll3.to_list()}")
    print(f"List 2: {ll4.to_list()}")
    
    merged_head = merge_sorted_lists(ll3.head, ll4.head)
    merged_list = LinkedList()
    merged_list.head = merged_head
    print(f"Merged: {merged_list.to_list()}")


if __name__ == "__main__":
    demo()
