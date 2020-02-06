class node:
    def __init__(self, data=None):
        self.data= data
        self.next= None
class linked_list:
    def __init__(self):
        self.head = node()
    def append(self, data):
        new_node=node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node
    def append(self, data1, data2):        
        new_node=node(data1)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node
        new_node=node(data2)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node
    def append(self, data1, data2, data3):        
        new_node=node(data1)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node
        new_node=node(data2)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node
        new_node=node(data3)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node
    def lenght(self):
        cur = self.head
        total = 0
        while cur.next != None:
            total+=1
            cur = cur.next
        return total
    def display(self):
        elems = []
        cur_node = self.head
        while cur_node.next != None:
            cur_node=cur_node.next
            elems.append(cur_node.data)
        print(elems)
    def get(self,index):
        if index >= self.lenght():
            print("Error: Out of range!")
            return None
        cur_index = 0
        cur_node=self.head
        while True:
            cur_node=cur_node.next
            if cur_index == index: return cur_node.data
            cur_index+=1
    def deleteForIndex(self,index):
        if index >= self.lenght():
            print("Error: Out of range!")
            return
        cur_index=0
        cur_node=self.head
        while True:
            last_node = cur_node
            cur_node = cur_node.next
            if cur_index==index:
                last_node.next=cur_node.next
                return
            cur_index+=1  
    def containData(self,data):
        cur = self.head
        cur_data = cur.data
        while cur.next != None:
            if cur_data==data:
                return True
            cur = cur.next
            cur_data = cur.data
        return False
    def deleteForData(self,data):
        if self.containData(data) == False:
            print("Error: Out of Data!")
            return
        cur_index=0
        cur_node=self.head
        while True:
            last_node = cur_node
            cur_node = cur_node.next
            if cur_node.data==data:
                last_node.next=cur_node.next
                return
            cur_index+=1

list = linked_list()
list.append(10,20,30)
list.display()
list.deleteForIndex(2)
list.display()
list.deleteForData(10)
list.display()