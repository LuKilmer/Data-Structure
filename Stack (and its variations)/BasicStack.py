class Node:
    def __init__(self,root:any):
        self.data=root
        self.next=None
    
class Stack:
    def __init__(self,root:any):
        self.root=Node(root)
    
    def __str__(self)->str:
        if self.root is not None:
            aux=self.root
            string = f'{aux.data}'
            while aux.next is not None:
                string+=f' {aux.next.data}'
                aux=aux.next
            return string
    
    def add(self,new):
        if self.root is None:
            self.root=Node(new)
        else:return self.real_add(self.root,new)
    
    def real_add(self,root,new):
        if root.next is None:
            root.next=Node(new)
        else:
            return self.real_add(root.next,new)

        
#main
stack=Stack(1)
stack.add(2)
stack.add(7)
stack.add(4)
stack.add(5)

print(stack)