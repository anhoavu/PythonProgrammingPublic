# Redo every exercises with Python list for linked list

class ListNode:
    def __init__(self, value = 0, next = None):
        self.value = value
        self.next = next

def printList(head):
    if head == None:
        print("∅")
        return

    print("[", head.value, "] → ", sep="", end="")
    printList(head.next)

def isInOrder(head):
    # Check if a linked list is in increasing order
    return True

def copyList(head):
    # Copy a linked list element by element
    return headNew

def linkedListToPythonList(head: ListNode):
    # Convert a linked list to a Python list
    return []

def listToLinkedList(L):
    # Convert a Python list to a linked list
    return head

def splitList(head: ListNode):
    # Return a pair of linked list by splitting the given linked list in the middle
    return (firstHalf, secondHalf)

def splitListEvenOdd(head: ListNode):
    # Return a pair of linked lists (their head nodes) containing elements at odd and even position only
    return (evenHead, oddHead)

def mergeSortedLists(head1: ListNode, head2: ListNode):
    # Merge two sorted linked lists
    return None

def sortLinkedList(head: ListNode):
    # Sort linked list using merge sort algorithm
    return None
