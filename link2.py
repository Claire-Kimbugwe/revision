

# find the nth last element in the linked list,given the head node, in the 
# below created linked list the 2nd last element would be node d with value 4.

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

def nth_last(n,node):
    # will use two markers leftmark starts at the beginning and rightmark 
    # starts at n, if rightmark gets to end of LList.then leftmark
    # will be at the target node
    leftmark=node
    rightmark= node
    # will set the rightmark to start at the nth node
    for i in range(n-1):
        if not rightmark.next:
            print(rightmark.next)
            raise LookupError("Error: n is larger than llist")
        rightmark= rightmark.next
        print(rightmark)
    print(f'the last one is : {rightmark}')
    while rightmark.next:
        rightmark=rightmark.next
        leftmark=leftmark.next

    return leftmark.val
#TEST
print(nth_last(2,a))
print('########################')
print(nth_last(0,a))
print('########################')
print(nth_last(1,a))
print(nth_last(9,a))
