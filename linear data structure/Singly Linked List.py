'''Singly Linked List
head -> have the reference of the first node
tail -> last node
node - > data | adress
linked list -> collection of node's

Functions :
1) to add
    - in the begning
    - in the end
    - in middle
    - when linked list is empty

2) to delet

3) print linked list
'''

class Node:
    def __init__(self,data):
        self.data = data
        self.link_to_next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None # head have the reference/link of the first node (its the first node of the linked list)

    def print_linked_list(self):
         if self.head == None:
             print('Linked List is empty')
         else:
             while self.head is not None:
                 print(self.head.data)
                 self.head = self.head.link_to_next

    def travel(self):
        if self.head is None:
            print('Linked List is empty')
        else:
            n = self.head
            count = 0
            print("LinkedList is :")
            while n is not None:
                count += 1
                # print("")
                print(n.data,end=' --> ')
                n = n.link_to_next
            print()
            print(f'Linked list had {count} vales totally')

    def add_in_begin(self,data):
        # n = self.head
        new_node = Node(data)
        new_node.link_to_next = self.head
        self.head = new_node

    def add_in_end(self,data):
        new_node = Node(data)
        if self.head is None:
           self.head = new_node
        else:
            n = self.head
            while n.link_to_next is not None: # this will stop when we get null reference
                n = n.link_to_next
            n.link_to_next = new_node

    def add_after_node(self,data,x):
        n = self.head
        while n is not None:
            if x == n.data:
                print('Found')
                break
            n = n.link_to_next
        if n is None:
            print(f"{x} element not found")
        else:
            new_node = Node(data)
            new_node.link_to_next = n.link_to_next
            n.link_to_next = new_node

    def add_before_node(self,data,x):
        if self.head == None:
            print("Singly Linked List is empty")

        n = self.head
        # to add in first node
        if self.head.data == x:
            new_node = Node(data)
            new_node.link_to_next = self.head
            self.head = new_node
        while n .link_to_next is not None:
            if n.link_to_next.data == x:
                break
            n = n.link_to_next

        if n.link_to_next is None:
            print(f"{x} element not found")
        else:
            new_node = Node(data)
            new_node.link_to_next =  n.link_to_next
            n.link_to_next = new_node

    def insert_empty(self,data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("Singly Linked List is not empty")

    def del_begin(self):
        if self.head == None:
            print("Empty Linked List canot perform deletion opreation")
        else:
            self.head = self.head.link_to_next

    def add_bulk_data(self):
        data = 'a b c d e f'.split()
        for i in data:
            self.add_in_begin(i)

    def del_last_node(self):
        if self.head is None:
            print(False)
        else:
            n = self.head
            while n.link_to_next.link_to_next is not None:
                n = n.link_to_next
            n.link_to_next = None

    def del_at_any_pos(self,x):
        if self.head is None:
            print("Tree is empyt")
        else:
            if x == self.head.data:
                self.del_begin()
            else:
                n = self.head
                while n.link_to_next is not None:
                    if x == n.data:
                        break
                n = n.link_to_next
                if n.link_to_next is None:
                    print(False)
                else:
                    n.link_to_next = n.link_to_next.link_to_next



if __name__ == '__main__':
    sll = SinglyLinkedList()
    sll.travel()
    sll.insert_empty(10)
    sll.travel()
    sll.add_in_begin(10)
    sll.add_in_begin(100)
    sll.add_after_node(1078,10)
    sll.add_in_end(1001)
    sll.travel()