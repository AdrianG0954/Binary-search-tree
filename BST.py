class BSTNode:
    def __init__(self, data, parent = None):
        self.data = data
        self.parent = parent
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

class BinarySearchTree:
    def __init__(self):
        self.root = None

    ################ Task 1 ################
    def insert(self, data):
        if self.root == None:
            self.root = BSTNode(data)
        else:
            self._add_child(data, self.root)    

        #use helper _add_child method to add children to existing parent

    def _add_child(self, data, p_node:BSTNode):
        if data == p_node.data: #duplicate items cannot be added
            return "Duplicates not allowed"

        #implement logic to recursively add a node at appropriate location
        if data < p_node.data:
            if p_node.left != None:
                self._add_child(data, p_node.left)
            else:
                p_node.left = BSTNode(data, p_node)
        else:
            if p_node.right != None:
                self._add_child(data, p_node.right)
            else:
                p_node.right = BSTNode(data, p_node)

    def get_max(self):
        if self.root.right == None:
            return self.root.data
        else:
            return self._get_right_child(self.root)

    def _get_right_child(self, node:BSTNode):
        #helper method to retrieve right node recursively
        if node.right == None:
            return node.data
        else:
            return self._get_right_child(node.right)        

    def get_min(self):
        if self.root.left == None:
            return self.root.data
        else:
            return self._get_left_child(self.root)

    def _get_left_child(self, node):
        #helper method to retrieve left node recursively
        if node.left == None:
            return node.data
        else:
            return self._get_left_child(node.left)

    def traverse_in_order(self, node, traversed_data):
        #traverse the tree in in-order fashion and keep
        #adding the elements in the traversed_data list
        if node == None:
            return traversed_data
        else:
            self.traverse_in_order(node.left, traversed_data)
            traversed_data.append(node.data)
            self.traverse_in_order(node.right, traversed_data)
            
    def delete(self, data):
        #starting from root node, pass the data and node
        #to be deleted to the helper node _remove_node
        if self.root != None:
            node = self.node_to_delete(data, self.root)
            self._remove_node(data, node)

    def node_to_delete(self, data, node):
        if data == node.data:
            return node
        
        if data < node.data:
            return self.node_to_delete(data, node.left)
        elif data > node.data:
            return self.node_to_delete(data, node.right)
        return node

    def _remove_node(self, data, node):
        
        if node.left == None and node.right == None: 
            self.remove_node_case1(data, node)

        elif node.left == None or node.right == None:
            # if node == root
            self.remove_node_case2(data, node)
        elif node.left != None and node.right != None:
            # if node == root
            self.remove_node_case3(data, node)
    
    def remove_node_case1(self,data, node):
        if node.parent.left.data == data:
            node.parent.left = None
            node = None    
        else:
            node.parent.right = None
            node = None
        return
    
    def remove_node_case2(self,data, node):
        if node.parent.left.data == data: 

            if node.left != None:
                node.parent.left = node.left
                node.left.parent = node.parent
                node.parent = None
                node.left = None
                node = None
            else:
                node.parent.left = node.right
                node.right.parent = node.parent
                node.parent = None
                node.right = None
                node = None
        else:
            if node.left != None:
                node.parent.right = node.left
                node.left.parent = node.parent
                node.parent = None
                node.left = None
                node = None
            else:
                node.parent.right = node.right
                node.right.parent = node.parent
                node.parent = None
                node.right = None
                node = None
        return

    def remove_node_case3(self,data, node):
        # deleting a node with two children
        predecessor = self._get_predecessor(node.left)
        node.data = predecessor.data
        self._remove_node(predecessor.data, predecessor)

    def _get_predecessor(self, node):
        if node.right:
            return self._get_predecessor(node.right)

        return node

    ################ Task 2 ################
    def traverse_pre_order(self, node, traversed_data):
        #traverse the tree in pre-order fashion and keep
        #adding the elements in the traversed_data list
        if node == None:
            return traversed_data
        else:
            traversed_data.append(node.data)
            self.traverse_pre_order(node.left, traversed_data)
            self.traverse_pre_order(node.right, traversed_data)

    def traverse_post_order(self, node, traversed_data):
        #traverse the tree in post-order fashion and keep
        #adding the elements in the traversed_data list
        if node == None:
            return traversed_data
        else:
            self.traverse_post_order(node.left, traversed_data)
            self.traverse_post_order(node.right, traversed_data)
            traversed_data.append(node.data)

    def __str__(self) -> str:
        return self.traverse_pre_order(self.root, [])  


if __name__ == "__main__":
    BST = BinarySearchTree()

    random_data = [12, 4, 20, 8, 1, 16, 27]
    for data in random_data:
        BST.insert(data)

    print("Testing Max...")

    assert(BST.get_max() == 27)
    print("PASSED!")

    print()

    print("Testing Min...")
    assert(BST.get_min() == 1)
    print("PASSED!")

    print()
    print("Testing In-order Traversal...")
    traversed_data = []
    BST.traverse_in_order(BST.root, traversed_data)
    assert(traversed_data == [1, 4, 8, 12, 16, 20, 27])
     
    print("PASSED!")

    print()
    print("Testing Deletion of root node with two child...")
    BST.delete(12)
    traversed_data2 = []
    BST.traverse_in_order(BST.root, traversed_data2)
    assert(traversed_data2 == [1, 4, 8, 16, 20, 27])
    print("PASSED!")

    print()
    print("Checking new root after deletion...")
    assert(BST.root.data == 8)
    print("VERIFIED!")


    print()
    print("Testing Deletion of node with one child...")
    BST.delete(4)
    traversed_data2 = []
    BST.traverse_in_order(BST.root, traversed_data2)
    assert(traversed_data2 == [1, 8, 16, 20, 27])
    print("PASSED!")

    print()
    print("Testing Deletion of leaf node...")
    BST.delete(1)
    traversed_data2 = []
    BST.traverse_in_order(BST.root, traversed_data2)
    assert(traversed_data2 == [8, 16, 20, 27])
    print("PASSED!")

    # ########## Task2 ##########
    print()
    # print("########## Task 2 ##########")
    BST2 = BinarySearchTree()
    #            12
    #       4         20
    #     1   8    16   27
    random_data = [12, 4, 20, 8, 1, 16, 27]
    for data in random_data:
        BST2.insert(data) 

    print()
    print("Testing Pre-order Traversal...")
    traversed_data3 = []
    BST2.traverse_pre_order(BST2.root, traversed_data3)
    assert(traversed_data3 == [12, 4, 1, 8, 20, 16, 27])
    print("PASSED!")

    print()
    print("Testing Post-order Traversal...")
    traversed_data4 = []
    BST2.traverse_post_order(BST2.root, traversed_data4)
    assert(traversed_data4 == [1, 8, 4, 16, 27, 20, 12])
    print("PASSED!")


    print()
    print("Testing deletion of node with two children...")
    BST2.delete(4)
    traversed_data5 = []
    BST2.traverse_in_order(BST2.root, traversed_data5)
    assert(traversed_data5 == [1, 8, 12, 16, 20, 27])
    print("PASSED!")
