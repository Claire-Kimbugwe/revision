
# Given the first node of a linkedlist reverse the 
# list in place and return new head

class Node:
    def __init__(self,val):
        self.val = val
        self.next= None
# instatiate nodes        
a=Node(1)
b=Node(2)
c=Node(3)
d=Node(4)
e=Node(5)
# create a linked list
a.next =b
b.next =c
c.next =d
d.next =e
# given the first node reverse the linkedlist in place, and return the head
def reverse(node):
    current =node
    nextnode=None
    previous=None

    while current:
        nextnode=current.next 
        current.next=previous
        previous = current
        current = nextnode
    return previous.val

print(reverse(a))