from django.test import TestCase

# Create your tests here.
class linked_Node:
    def __init__(self,value) :
        self.value = value
        self.next = None

list = linked_Node(0)
n1 = linked_Node(1)
n2 = linked_Node(2)
n3 = linked_Node(3)
n4 = linked_Node(4)
list.next = n1
n1.next = n2
n2.next = n3
n3.next = n4

print(list.next.next.next.value)