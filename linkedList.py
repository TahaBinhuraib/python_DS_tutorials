class Node():
    def __init__(self,item):
        self.item = item
        self.next = None

class linkedList:
    def __init__(self):
        self.head = None
    
    def isEmpty(self):
        """Checks if linked list is empty or not"""
        if(self.head == None):
            return True
        else:
            return False
    
    def appendNode(self, node):
        if(self.isEmpty()):
            self.head = node
        else:
            temp = self.head
            while(temp.next != None):
                temp = temp.next
            temp.next = node
        print(f'appended node {node.item}')
    
    def __repr__(self):
        node = self.head
        nodes = []
        while(node != None):
            nodes.append(node.item)
            node = node.next
        nodes.append("None")

        return " --> ".join(nodes)



def main():
    n1 = Node(str(2))
    n2 = Node(str(3))
    ll = linkedList()
    ll.appendNode(n1)
    ll.appendNode(n2)
    print(ll)

if __name__ == "__main__":
    main()


