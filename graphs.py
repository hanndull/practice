
class Node:
    def __init__(self, name):
        self.children = [] #initiates empty list to be added to via add_child
        self.name = name

    def add_child(self, node):
        '''Must add pre-existing node'''
        self.children.append(node) 
        return self

    def breadth_first_search(self, array):
        '''check through all nodes of graph, and add them to array 
        in breadth-first order, using a list as a queue
        '''
        queue = []
        queue.append(self)
        
        while queue:
            current_node = queue.pop(0)
            
            if current_node.name not in array:
                array.append(current_node.name)

            for child in current_node.children:
                
                if child.name not in array: #Added this in for purposes of graphs 
                    queue.append(child)
        
        return array

#----------------------------------------------------------------------------
# TEST 1 -- tree           
    
test3 = Node("A")
test3.add_child(Node("B"))
test3.children[0].add_child(Node("C"))
test3.children[0].children[0].add_child(Node("D")).add_child(Node("E"))
test3.children[0].children[0].children[0].add_child(Node("F"))

assert test3.breadth_first_search([]) == ["A", "B", "C", "D", "E", "F"]

#----------------------------------------------------------------------------
# TEST 2 -- graph

h = Node("Hannah")
jas = Node('Jason')
jan = Node('Jan')
b = Node('Belinda')
h.add_child(jas).add_child(jan).add_child(b)
jas.add_child(h).add_child(jan)
jan.add_child(h).add_child(jas)
b.add_child(h)

assert h.breadth_first_search([]) == ['Hannah', 'Jason', 'Jan', 'Belinda']

assert b.breadth_first_search([]) == ['Belinda', 'Hannah', 'Jason', 'Jan']

















