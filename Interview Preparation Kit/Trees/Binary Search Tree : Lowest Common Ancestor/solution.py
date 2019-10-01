# Not the cleanest or most efficient implementation. TODO refactor and improve upon logic

class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''

def lca(root, v1, v2):
    node1 = root
    node2 = root
    v1_ancestors = []
    v2_ancestors = []
    
    while(node1.info != v1):
        #print(node1.info, v1)
        if (v1 > node1.info):
            v1_ancestors.append(node1)
            node1 = node1.right
        else:
            v1_ancestors.append(node1)
            node1 = node1.left
    v1_ancestors.append(node1)
    while(node2.info != v2):
        #print(node2.info, v2)
        if (v2 > node2.info):
            v2_ancestors.append(node2)
            node2 = node2.right
        else:
            v2_ancestors.append(node2)
            node2 = node2.left
    v2_ancestors.append(node2)
    if (len(v1_ancestors)== 0 or len(v2_ancestors)==0):
        return 
    for x in range(len(v1_ancestors)-1,-1,-1):
         for y in range(len(v2_ancestors)-1,-1,-1):
             if (v1_ancestors[x] == v2_ancestors[y]):
                 return (v1_ancestors[x])


        

tree = BinarySearchTree()
