class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
class LinkedList:
    def __init__(self,head=None):
        self.head=head
    def length_of(self):
        count=0
        current_node=self.head
        while current_node is not None:
            count+=1
            current_node=current_node.next
        return count
    def insert_at_end(self,data):
        node=Node(data)
        if self.head is None:
            self.head=node
        else:
            current_node=self.head
            while current_node.next is not None:
                current_node=current_node.next
            current_node.next=node
    def insert_at_start(self,data):
        node=Node(data,self.head)
        self.head=node
    def insert_at(self,data,index):
        current_node=self.head
        count=0
        if index==0:
            self.insert_at_start(data)
        else:
            while current_node :
                if count==index-1:
                    current_node.next=Node(data,current_node.next)
                    break
                count+=1
                current_node=current_node.next
    def delete_at_start(self):
        self.head=self.head.next
    def delete_at_end(self):
        current_node=self.head
        count=0
        while current_node:
            if count==(self.length_of())-2:
                current_node.next=None
            count+=1
            current_node=current_node.next
    def delete_at(self,index):
        current_node=self.head
        count=0
        while current_node:
            if count==index-1:
                current_node.next=current_node.next.next
            current_node=current_node.next
            count+=1
    def reverse(self):
        prev=None
        current_node=self.head
        while current_node:
            next_node=current_node.next
            current_node.next=prev
            prev=current_node
            current_node=next_node
        self.head=prev
    def printLinkedList(self):
        current_node=self.head
        while current_node is not None:
            print(current_node.data,"-->",end=" ")
            current_node=current_node.next
        print()




            
li=LinkedList()
for i in range(1,11):
    li.insert_at_end(str(i))
li.printLinkedList()
li.insert_at_start("10")
li.insert_at("20",1)
li.printLinkedList()
li.reverse()
li.printLinkedList()
'''
current_node=node1
while True:
    print(current_node.data)
    if current_node.next is None:
        print(None)
        break
    else:
        current_node=current_node.next '''